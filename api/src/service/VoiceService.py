from python_helper import Constant as c
from python_helper import EnvironmentHelper, ObjectHelper, RandomHelper, StringHelper, log
from python_framework import Service, ServiceMethod, EnumItem

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
             log.warning(self.speakAll, 'Not possible to speak', exception=exception, muteStackTrace=True)
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
             log.warning(self.speakAll, 'Not possible to speak', exception=exception, muteStackTrace=True)
        return serviceReturn


    @ServiceMethod(requestClass=[[AudioDataDto.AudioDataRequestDto]])
    def createAll(self, dtoList):
        existingModelList = self.repository.audioData.findAllByKeyIn([dto.key for dto in dtoList if dto])
        return self.mapper.audioData.fromModelListToResponseDtoList(
            self.persistAll(
                self.mapper.audioData.fromRequestDtoListToModelList([
                    dto
                    for dto in dtoList
                    if dto and dto.key not in [
                        model.key for model in existingModelList
                    ]
                ])
            )
        )

    @ServiceMethod(requestClass=[[AudioData.AudioData]])
    def persistAll(self, modelList):
        return self.repository.audioData.saveAll(modelList)
