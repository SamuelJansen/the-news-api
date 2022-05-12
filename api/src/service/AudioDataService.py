import datetime

from python_helper import Constant as c
from python_helper import EnvironmentHelper, ObjectHelper, RandomHelper, StringHelper, log
from python_framework import Service, ServiceMethod, EnumItem

import AudioDataDto
import AudioData


@Service()
class AudioDataService :

    @ServiceMethod(requestClass=[[AudioDataDto.AudioDataRequestDto], datetime.date])
    def createAll(self, dtoList, date):
        existingModelList = self.repository.audioData.findAllByKeyInAndDate([dto.key for dto in dtoList if dto], date)
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


    @ServiceMethod()
    def findAllByDate(self, date):
        return self.mapper.audioData.fromModelListToResponseDtoList(self.repository.audioData.findAllByDate(date))


    @ServiceMethod()
    def countByDate(self, date):
        return self.repository.audioData.countByDate(date)
