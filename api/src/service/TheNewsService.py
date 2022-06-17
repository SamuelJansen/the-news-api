import datetime

from python_helper import Constant as c
from python_helper import log, StringHelper, ObjectHelper, DateTimeHelper, FileOperation
from python_framework import Service, ServiceMethod, EnumItem
from notification_manager_api import NotificationDestiny

from config import TheNewsConfig
from domain.ContentType import ContentType
from enumeration.EmailContact import EmailContact
from enumeration.EmailBox import EmailBox
from enumeration.Voice import Voice
from enumeration.NewsStatus import NewsStatus
from constant import NewsConstant
import EmailStaticHelper
import AudioDataDto
import News


EMAIL_SUBJECT_KEY = 'subject'
TEXT_PLAIN_LIST_KEY = 'textPlainList'
TEXT_HTML_LIST_KEY = 'textHtmlList'


@Service()
class TheNewsService:

    @ServiceMethod(requestClass=[[AudioDataDto.AudioDataRequestDto]])
    def finishTodayNewsUpdate(self, audioDataRequestDtoList):
        log.status(self.finishTodayNewsUpdate, f'Finishing today news update')
        newsModel = self.createOrUpdateNewsModel(DateTimeHelper.dateNow(), NewsStatus.PROCESSING)
        audioDataResponseDtoList = []
        try:
            audioDataResponseDtoList = self.service.audioData.createOrUpdateAll(audioDataRequestDtoList, newsModel.date)
            if 0 == len(audioDataResponseDtoList):
                existingAudioDatas = self.service.audioData.countByDate(newsModel.date)
                if 0 == existingAudioDatas:
                    self.updateNewsModel(newsModel, NewsStatus.ERROR)
                    raise Exception(f'Error while creating today news. No audio datas were created')
                elif existingAudioDatas < len(audioDataRequestDtoList):
                    self.updateNewsModel(newsModel, NewsStatus.ERROR)
                    raise Exception(f'Not enought audio datas were created this time. There are only {existingAudioDatas} existing audio datas. Should be {len(audioDataRequestDtoList)}')
            self.updateNewsModel(newsModel, NewsStatus.FINISHED)

            successMessage = f'Today news created'
            log.status(self.finishTodayNewsUpdate, successMessage)
            self.service.notification.notifySuccess(successMessage)
        except Exception as exception:
            errorMessage = 'Not possible to finish today news update'
            log.failure(self.finishTodayNewsUpdate, errorMessage, exception=exception, muteStackTrace=True)
            self.service.notification.notifyError(errorMessage)
            self.updateNewsModel(newsModel, NewsStatus.ERROR)
            raise exception
        return audioDataResponseDtoList


    @ServiceMethod(requestClass=[datetime.date, EnumItem])
    def createOrUpdateNewsModel(self, date, status):
        log.status(self.createOrUpdateNewsModel, f'Creating news model with date: {date} and status: {status}')
        key = self.buildNewsKey(date)
        newsModel = self.getOrCreateNewsByKey(key)
        newsModel.status = status
        return self.repository.news.save(newsModel)


    @ServiceMethod(requestClass=[News.News, EnumItem])
    def updateNewsModel(self, model, status):
        log.status(self.updateNewsModel, f'Updating news model with status: {status}')
        model.status = status
        return self.repository.news.save(model)


    @ServiceMethod(requestClass=[EnumItem])
    def getOrCreateNewsByKey(self, key):
        if self.newsExistsByKey(key):
            return self.getNewsByKey(key)
        else:
            return News.News(
                key = key,
                date = DateTimeHelper.forcedlyGetDate(key.replace(f'{NewsConstant.FILE_PREFIX_NAME}{c.DASH}', c.BLANK)),
                status = NewsConstant.DEFAULT_STATUS
            )


    @ServiceMethod()
    def getOrCreateTodayNewsModel(self):
        log.status(self.getOrCreateTodayNewsModel, f'Guetting today news model')
        newsModel = self.repository.news.findMostRecentByStatus(NewsConstant.END_STATUS)
        if ObjectHelper.isNone(newsModel):
            newsModel = self.getOrCreateNewsByKey(self.buildNewsKey(DateTimeHelper.dateNow()))
        return newsModel


    @ServiceMethod(requestClass=[str])
    def newsExistsByKey(self, key):
        return self.repository.news.existsByKey(key)


    @ServiceMethod(requestClass=[str])
    def getNewsByKey(self, key):
        return self.repository.news.findByKey(key)


    @ServiceMethod()
    def buildNewsKey(self, key):
        return f'{NewsConstant.FILE_PREFIX_NAME}{c.DASH}{key}'


    @ServiceMethod()
    def buildTodayNewsHtmlFileName(self, newsKey):
        return f'{newsKey}{c.DOT}{NewsConstant.FILE_EXTENSION}'


    def getTodayNewsHtmlFileName(self):
        return self.buildTodayNewsHtmlFileName(self.getOrCreateTodayNewsModel().key)


    @ServiceMethod()
    def startTodaysNewsUpdate(self):
        logMessage = f'Updating today news'
        log.status(self.startTodaysNewsUpdate, logMessage)
        self.service.notification.notifyDebugTo(logMessage, [NotificationDestiny.TELEGRAM])
        try:
            newsModel = self.createOrUpdateNewsModel(DateTimeHelper.dateNow(), NewsStatus.CREATED)

            emailBody = self.getEmailBodyList(TheNewsConfig.TODAY_NEWS_EMAIL_AMOUNT)
            self.updateNewsModel(newsModel, NewsStatus.PROCESSING_TEXT)

            subject = emailBody.get(EMAIL_SUBJECT_KEY, c.BLANK)
            emailBodySentenceList = self.getEmailBodySentenceList(subject, emailBody.get(TEXT_PLAIN_LIST_KEY, []))[-1]
            emailHtml = EmailStaticHelper.buildHtml(emailBody.get(TEXT_HTML_LIST_KEY, c.BLANK))[-1]
            self.client.theNews.writeContent(self.buildTodayNewsHtmlFileName(newsModel.key), subject, emailHtml, FileOperation.OVERRIDE_TEXT)

            logMessage = f'Creatting today news voice overs'
            log.status(self.startTodaysNewsUpdate, logMessage)
            self.service.notification.notifyDebugTo(logMessage, [NotificationDestiny.TELEGRAM])
            # self.service.voice.createAudios(emailBodySentenceList, Voice.ANTONIO)

            self.updateNewsModel(newsModel, NewsStatus.PROCESSING_AUDIO)

        except Exception as exception:
            self.updateNewsModel(newsModel, NewsStatus.ERROR)
            errorMessage = 'Error while updating today news'
            log.error(self.startTodaysNewsUpdate, errorMessage, exception=exception)
            self.service.notification.notifyError(errorMessage)


    @ServiceMethod()
    def getTodaysNewsAudios(self):
        log.status(self.startTodaysNewsUpdate, f'Getting today news audio data')
        return self.service.audioData.findAllByDate(self.getOrCreateTodayNewsModel().date)


    @ServiceMethod(requestClass=[int])
    def getEmailBodyList(self, emailAmount):
        plainTextEmailList = []
        while 0 == len(plainTextEmailList):
            messageList = self.service.email.getMessages(emailAmount, EmailContact.THE_NEWS.email, EmailBox.INBOX)
            if ObjectHelper.isNotEmpty(messageList[-1].get(EMAIL_SUBJECT_KEY)):
                subject = messageList[-1].get(EMAIL_SUBJECT_KEY)[-1]
                plainTextEmailList = messageList[-1].get(ContentType.TEXT_PLAIN)
                htmlTextContentList = messageList[-1].get(ContentType.TEXT_HTML)
                emailBody = {
                    EMAIL_SUBJECT_KEY: subject,
                    TEXT_PLAIN_LIST_KEY: plainTextEmailList,
                    TEXT_HTML_LIST_KEY: htmlTextContentList
                }
            emailAmount += 1
        return emailBody


    @ServiceMethod(requestClass=[int, [str]])
    def getEmailBodySentenceList(self, subject, plainTextEmailList):
        logMessage = 'Parsing email body sentences'
        log.prettyPython(self.getEmailBodySentenceList, logMessage, plainTextEmailList, logLevel=log.STATUS)
        self.service.notification.notifyDebugTo(logMessage, [NotificationDestiny.TELEGRAM])
        totalEmailBodySentenceList = []
        for plainTextEmail in plainTextEmailList:
            compiledEmailBodyList = EmailStaticHelper.getCompiledEmailBodyList(plainTextEmail)
            totalEmailBodySentenceList.append(compiledEmailBodyList)
            log.prettyPython(self.getEmailBodySentenceList, 'Email body sentences', compiledEmailBodyList, logLevel=log.STATUS)

            logMessage = f'There are a total of {len(compiledEmailBodyList)} email body sentences'
            log.status(self.getEmailBodySentenceList, logMessage)
            self.service.notification.notifyDebugTo(logMessage, [NotificationDestiny.TELEGRAM])
        return totalEmailBodySentenceList
