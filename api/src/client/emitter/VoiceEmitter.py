from python_framework import Serializer, HttpStatus, JwtConstant
from queue_manager_api import MessageEmitter, MessageEmitterMethod, MessageDto

from config import VoiceQueueConfig, VoiceClientConfig


@MessageEmitter(
    url = VoiceQueueConfig.CREATE_TODAY_NEWS_EMITTER_URL,
    timeout = VoiceQueueConfig.CREATE_TODAY_NEWS_EMITTER_TIMEOUT,
    headers = {
        'Content-Type': 'application/json',
        JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {VoiceQueueConfig.CREATE_TODAY_NEWS_EMITTER_API_KEY}'
    }
    , muteLogs = False
    # , logRequest = True
    # , logResponse = True
)
class VoiceEmitter:

    @MessageEmitterMethod(
        url = '/message/emitter',
        queueKey = VoiceQueueConfig.CREATE_TODAY_NEWS_QUEUE_KEY,
        requestHeadersClass=[dict],
        requestClass=[[dict]]
        # responseClass=[[dict]]
        , logRequest = True
        , logResponse = True
    )
    def createAll(self, dto, headers=None):
        return self.emit(
            headers = headers,
            messageHeaders = {
                JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {VoiceClientConfig.API_KEY}'
            },
            body = dto
        )
