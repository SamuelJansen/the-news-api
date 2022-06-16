from python_helper import Constant as c
from python_helper import EnvironmentHelper, ObjectHelper, RandomHelper, StringHelper, log
from python_framework import Service, ServiceMethod, EnumItem
from notification_manager_api import NotificationDestiny

import AudioDataDto
import AudioData


@Service()
class VoiceService :


    @ServiceMethod(requestClass=[[str], EnumItem])
    def getAudios(self, textList, voice):
        serviceReturn = None
        try:
            serviceReturn = self.client.voice.speakAll([
                {
                    'text': text,
                    'voice': voice,
                    'muted': True
                } for text in textList
            ])
        except Exception as exception:
            errorMessage = 'Not possible to get audios'
            log.warning(self.speakAll, errorMessage, exception=exception, muteStackTrace=True)
            self.service.notification.notifyWarningTo(errorMessage, [NotificationDestiny.TELEGRAM])
        return serviceReturn


    @ServiceMethod(requestClass=[[str], EnumItem])
    def createAudios(self, textList, voice):
        serviceReturn = None
        try:
            serviceReturn = self.emitter.voice.createAll([
                {
                    'text': text,
                    'voice': voice,
                    'muted': True
                } for text in textList
            ])
        except Exception as exception:
            errorMessage = 'Not possible to create audios'
            log.warning(self.speakAll, errorMessage, exception=exception, muteStackTrace=True)
            self.service.notification.notifyWarningTo(errorMessage, [NotificationDestiny.TELEGRAM])
        return serviceReturn
