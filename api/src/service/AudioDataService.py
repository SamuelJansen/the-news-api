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
        log.prettyPython(self.createOrUpdateAll, 'Receiving audio datas', [dto.key for dto in dtoList], logLevel=log.STATUS)
        requestKeyList = [dto.key for dto in dtoList if dto and dto.key]
        assert 0 < len(requestKeyList), f'Request dto must have defined keys. Keys: {requestKeyList}'

        existingModelList = self.repository.audioData.findAllByDateAndKeyIn(date, requestKeyList)
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
        assert len(dtoList) == len(modelList), f'Missing audio datas werent created. Causes dtoList: {[dto.key for dto in dtoList]}, modelList: {[model.key for model in modelList]}. Request length: {len(dtoList)}, model length: {len(modelList)}'

        self.deleteAll(self.repository.audioData.findAllByDateAndKeyNotIn(date, requestKeyList))

        return self.mapper.audioData.fromModelListToResponseDtoList(self.persistAll(modelList))


    @ServiceMethod(requestClass=[[AudioData.AudioData]])
    def persistAll(self, modelList):
        log.prettyPython(self.persistAll, 'Persisting audios', [model.key for model in modelList], logLevel=log.STATUS)
        return self.repository.audioData.saveAll(modelList)


    @ServiceMethod(requestClass=[[AudioData.AudioData]])
    def deleteAll(self, modelList):
        log.prettyPython(self.deleteAll, 'Deleting audios', [model.key for model in modelList], logLevel=log.STATUS)
        return self.repository.audioData.deleteAll(modelList)


    @ServiceMethod()
    def findAllByDate(self, date):
        return self.mapper.audioData.fromModelListToResponseDtoList(self.repository.audioData.findAllByDateOrderedByOrder(date))


    @ServiceMethod()
    def countByDate(self, date):
        return self.repository.audioData.countByDate(date)
