from python_helper import Constant as c
from python_helper import log, StringHelper, ObjectHelper, DateTimeHelper
from python_framework import Service, ServiceMethod


from config import TheNewsConfig
from domain.FileOperation import FileOperation
from domain.ContentType import ContentType
from enumeration.EmailContact import EmailContact
from enumeration.EmailBox import EmailBox
from enumeration.Voice import Voice


EMAIL_SUBJECT_KEY = 'subject'
TEXT_PLAIN_LIST_KEY = 'textPlainList'
TEXT_HTML_KEY = 'textHtml'


@Service()
class TheNewsService:

    @ServiceMethod()
    def updateTodaysNews(self):
        log.status(self.updateTodaysNews, f'Updating today news')
        emailBody = self.getEmailBodyList(TheNewsConfig.TODAY_NEWS_EMAIL_AMOUNT)
        subject = emailBody.get(EMAIL_SUBJECT_KEY, c.BLANK)
        emailBodySentenceList = self.getEmailBodySentenceList(
            subject,
            emailBody.get(TEXT_PLAIN_LIST_KEY, []),
            emailBody.get(TEXT_HTML_KEY, c.BLANK)
        )[-1]

        rawHtml = emailBody.get(TEXT_HTML_KEY, c.BLANK)
        collectedBody = []
        for index, bodyPart in enumerate(rawHtml.split('<body')):
            if index>0:
                splitHtml = bodyPart.split('>')
                parsedBodyPart = StringHelper.join(
                    [
                        splitHtml[0],
                        '<button onClick="handlePlayClick()">voice over</button',
                        *splitHtml[1:]
                    ],
                    character='>'
                )
            else:
                parsedBodyPart = bodyPart
            collectedBody.append(parsedBodyPart)
        html = StringHelper.join(collectedBody, character='<body')
        html = html.replace('</body>', '<script src="{{staticUrl}}/utils.js" type="text/javascript"></script></body>')

        self.client.theNews.writeContent(TheNewsConfig.TODAY_NEWS_FILE_NAME, subject, html, FileOperation.OVERRIDE_TEXT)
        self.service.voice.createAudios(emailBodySentenceList, Voice.ANTONIO)
        log.status(self.updateTodaysNews, f'Todays news updated')


    @ServiceMethod()
    def getTodaysNewsAudios(self):
        log.status(self.updateTodaysNews, f'Getting today news audio data')
        return self.mapper.audioData.fromModelListToResponseDtoList(
            self.repository.audioData.findAllByDate(DateTimeHelper.dateNow())
        )


    @ServiceMethod(requestClass=[int])
    def getEmailBodyList(self, emailAmount):
        plainTextEmailList = []
        while 0 == len(plainTextEmailList):
            messageList = self.service.email.getMessages(emailAmount, EmailContact.THE_NEWS.email, EmailBox.INBOX)
            if ObjectHelper.isNotEmpty(messageList[-1].get(EMAIL_SUBJECT_KEY)):
                subject = messageList[-1].get(EMAIL_SUBJECT_KEY)[-1]
                plainTextEmailList = messageList[-1].get(ContentType.TEXT_PLAIN)
                htmlTextContent = messageList[-1].get(ContentType.TEXT_HTML)[-1]
                emailBody = {
                    EMAIL_SUBJECT_KEY: subject,
                    TEXT_PLAIN_LIST_KEY: plainTextEmailList,
                    TEXT_HTML_KEY: htmlTextContent
                }
            emailAmount += 1
        return emailBody


    @ServiceMethod(requestClass=[int, [str], str])
    def getEmailBodySentenceList(self, subject, plainTextEmailList, htmlTextContent):
        totalEmailBodySentenceList = []
        for plainTextEmail in plainTextEmailList:
            isMarketing = False
            notFilteredEmailBodySentenceList = []
            for emailBodySentence in [
                emailBodySentenceUnity
                for emailBodySentenceUnity in [
                    possibleEmailBodySentence.replace(f'\r', c.BLANK)
                    for possibleEmailBodySentence in plainTextEmail.split(f'{c.NEW_LINE}')
                ]
                if StringHelper.isNotBlank(emailBodySentenceUnity)
            ]:
                if (
                    emailBodySentence.startswith('CLIQUE PARA COMPARTILHAR') or
                    emailBodySentence.endswith('FL') or
                    emailBodySentence.endswith('QUIZ THE NEWS') or
                    emailBodySentence.endswith('QUIZ') or
                    emailBodySentence.endswith('EDIÇÃO ESPECIAL DE SÁBADO') or
                    emailBodySentence.endswith('PROGRAMA DE INDICAÇÃO') or
                    emailBodySentence.endswith('GIVEAWAY DO DÊNIUS')
                ):
                    isMarketing = True
                elif emailBodySentence.split()[-1].isupper():
                    isMarketing = False

                if not isMarketing:
                    if (not isMarketing and not emailBodySentence.split()[-1].isupper()):
                        notFilteredEmailBodySentenceList.append(emailBodySentence)
                    else:
                        upperCaseWords = c.BLANK
                        for charactere in reversed(emailBodySentence):
                            if charactere.isupper() or (c.SPACE == charactere and not c.BLANK == upperCaseWords):
                                upperCaseWords = f'{charactere}{upperCaseWords}'
                            elif c.BLANK == upperCaseWords:
                                upperCaseWords = c.BLANK
                            else:
                                break
                        sentence = emailBodySentence.replace(upperCaseWords, c.BLANK)
                        if StringHelper.isBlank(sentence):
                            sentence = lastSentence
                        if upperCaseWords.startswith('PATROCINADO POR'):
                            isMarketing = True
                        if not isMarketing:
                            notFilteredEmailBodySentenceList.append(sentence.strip())
                            notFilteredEmailBodySentenceList.append(upperCaseWords.strip())

                lastSentence = emailBodySentence

            filteredEmailBodySentenceList = [
                emailBodySentence if not '[http' in emailBodySentence else ' '.join([
                    ' '.join([
                        p if not p.startswith('s://') else f'{c.NEW_LINE}[Link]{c.NEW_LINE}'
                        for p in part.split(']')
                    ]) for part in emailBodySentence.split('[http')
                ])
                for emailBodySentence in notFilteredEmailBodySentenceList
            ]

            emailBodySentenceList = [
                StringHelper.join(emailBodySentence.strip().split(), character=c.SPACE)
                for filteredEmailBodySentence in filteredEmailBodySentenceList
                for emailBodySentence in filteredEmailBodySentence.split(c.NEW_LINE)
                if (
                    StringHelper.isNotBlank(emailBodySentence.strip()) and
                    not c.DOT == emailBodySentence.strip() and
                    not '[Link]' == emailBodySentence.strip()
                )
            ]

            recentensedList = []
            for sentence in emailBodySentenceList:
                if sentence.startswith(c.DOT_SPACE) or sentence.startswith(c.COMA_SPACE):
                    if sentence.startswith(c.DOT_SPACE):
                        recentensedList[-1] = f'{recentensedList[-1]}{c.DOT}'
                    else:
                        recentensedList[-1] = f'{recentensedList[-1]}{c.COMA}'
                    recentensedList.append(sentence[2:].strip())
                else:
                    recentensedList.append(sentence.strip())

            emailBodySentenceList = []
            for sentence in recentensedList:
                if sentence.startswith(c.DOT) or sentence.startswith(c.COMA):
                    if sentence.startswith(c.DOT):
                        emailBodySentenceList[-1] = f'{emailBodySentenceList[-1]}{c.DOT}'
                    else:
                        emailBodySentenceList[-1] = f'{emailBodySentenceList[-1]}{c.COMA}'
                    emailBodySentenceList.append(sentence[1:].strip())
                else:
                    emailBodySentenceList.append(sentence.strip())

            emailBodySentenceList = [
                sentence\
                    .replace(c.BACK_SLASH_DOUBLE_QUOTE, c.SINGLE_QUOTE)\
                    .replace(c.DOUBLE_QUOTE, c.SINGLE_QUOTE)\
                    .replace('&nbsp;', c.BLANK)\
                    .replace('\U0001fa99', c.BLANK)\
                    .replace(c.AND, f'{c.SPACE}and{c.SPACE}')
                for sentence in emailBodySentenceList
            ]

            emailBodySentenceList = [
                sentence
                for sentence in emailBodySentenceList
                if not sentence.lower().startswith('(imagem') and not sentence.lower().startswith('(gif') and not sentence.lower().startswith('(foto')
            ]

            compiledEmailBodyList = []
            for sentence in emailBodySentenceList:
                if (StringHelper.isNotBlank(sentence)):
                    if sentence.isupper():
                        compiledEmailBodyList = [*compiledEmailBodyList[:-1], sentence, compiledEmailBodyList[-1]]
                    elif 3 > len(sentence):
                        compiledEmailBodyList[-1] = f'{compiledEmailBodyList[-1]}{c.SPACE}{sentence}'
                    elif sentence not in compiledEmailBodyList:
                        compiledEmailBodyList.append(sentence)

            totalEmailBodySentenceList.append(compiledEmailBodyList)

            log.prettyPython(self.getEmailBodySentenceList, 'Email body sentences', compiledEmailBodyList, logLevel=log.STATUS)
            log.status(self.getEmailBodySentenceList, f'There is a total of {len(compiledEmailBodyList)} email body sentences')
        return totalEmailBodySentenceList
