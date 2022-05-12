import datetime

from python_helper import Constant as c
from python_helper import EnvironmentHelper, ObjectHelper, RandomHelper, StringHelper, log, DateTimeHelper
from python_framework import Service, ServiceMethod, EnumItem

import AudioDataDto
import AudioData


@Service()
class AudioDataService :

    @ServiceMethod(requestClass=[[AudioDataDto.AudioDataRequestDto], datetime.date])
    def createOrUpdateAll(self, dtoList, date):
        existingModelList = self.repository.audioData.findAllByKeyInAndDate([dto.key for dto in dtoList if dto], date)
        newModels = self.mapper.audioData.fromRequestDtoListToModelList([
            dto
            for dto in dtoList
            if dto and dto.key not in [
                model.key for model in existingModelList
            ]
        ])
        modelList = [
            self.mapper.audioData.overrideModelUpdate(model, date, dtoList.index(dto))
            for dto in dtoList
            for model in [*existingModelList, *newModels]
            if dto.key == model.key
        ]
        assert len(dtoList) == len(modelList), f'Missing audio datas werent created. dtoList: {dtoList} modelList: {modelList}'
        return self.mapper.audioData.fromModelListToResponseDtoList(self.persistAll(modelList))


    @ServiceMethod(requestClass=[[AudioData.AudioData]])
    def persistAll(self, modelList):
        return self.repository.audioData.saveAll(modelList)


    @ServiceMethod()
    def findAllByDate(self, date):
        return self.mapper.audioData.fromModelListToResponseDtoList(self.repository.audioData.findAllByDateOrderedByOrder(date))


    @ServiceMethod()
    def countByDate(self, date):
        return self.repository.audioData.countByDate(date)
