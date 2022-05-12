from python_helper import log
from python_framework import HttpStatus
from queue_manager_api import MessageListener, MessageListenerMethod

from ApiKeyContext import ApiKeyContext
from config import TheNewsQueueConfig
import AudioDataDto


@MessageListener(
    timeout = TheNewsQueueConfig.PERSIST_TODAY_NEWS_VOICE_LISTENER_TIMEOUT
    , muteLogs = False
    , logRequest = True
    , logResponse = True
)
class TheNewsListener:

    @MessageListenerMethod(url = '/listener/audio',
        requestClass = [[AudioDataDto.AudioDataRequestDto]],
        apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.USER, ApiKeyContext.API],
        runInAThread = True
        , logRequest = True
        , logResponse = True
    )
    def acceptAudioSpeakList(self, dtoList):
        return self.service.theNews.finishTodayNewsCreation(dtoList), HttpStatus.ACCEPTED
