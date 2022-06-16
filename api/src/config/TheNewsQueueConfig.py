from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


PERSIST_TODAY_NEWS_VOICE_LISTENER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.persist-today-news-voice.listener.timeout')
