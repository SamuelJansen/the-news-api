from python_helper import Constant as c
from python_framework import Mapper, MapperMethod

from constant import VoiceManagerApiConstant
from config import VoiceClientConfig
import AudioData
import AudioDataDto

@Mapper()
class AudioDataMapper:

    @MapperMethod(requestClass=[[AudioDataDto.AudioDataRequestDto]], responseClass=[[AudioData.AudioData]])
    def fromRequestDtoListToModelList(self, dtoList, modelList):
        self.overrideModelListStaticUrl(modelList)
        return modelList

    @MapperMethod(requestClass=[[AudioData.AudioData]], responseClass=[[AudioDataDto.AudioDataResponseDto]])
    def fromModelListToResponseDtoList(self, modelList, dtoList):
        return dtoList

    @MapperMethod(requestClass=[AudioDataDto.AudioDataRequestDto], responseClass=[AudioData.AudioData])
    def fromRequestDtoToModel(self, dto, model):
        self.overrideModelStaticUrl(model)
        return model

    @MapperMethod(requestClass=[AudioData.AudioData], responseClass=[AudioDataDto.AudioDataResponseDto])
    def fromModelToResponseDto(self, model, dto):
        return dto

    @MapperMethod(requestClass=[[AudioData.AudioData]])
    def overrideModelListStaticUrl(self, modelList):
        for model in modelList:
            self.overrideModelStaticUrl(model)

    @MapperMethod(requestClass=[AudioData.AudioData])
    def overrideModelStaticUrl(self, model):
        model.staticUrl = f'{VoiceClientConfig.BASE_URL}{VoiceManagerApiConstant.AUDIO_DATA_STATIC_URI}{c.SLASH}{model.key}'
