from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


CREATE_TODAY_NEWS_QUEUE_KEY = globalsInstance.getSetting('queue-manager-api.voice-manager-api.create-today-news-voice.queue-key')

CREATE_TODAY_NEWS_EMITTER_URL = globalsInstance.getSetting('queue-manager-api.base-url')
CREATE_TODAY_NEWS_EMITTER_API_KEY = globalsInstance.getSetting('queue-manager-api.api-key')
CREATE_TODAY_NEWS_EMITTER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.voice-manager-api.create-today-news-voice.emitter.timeout')

PERSIST_TODAY_NEWS_VOICE_LISTENER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.voice-manager-api.persist-today-news-voice.listener.timeout')
