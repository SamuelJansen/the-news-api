from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()

BASE_URL = globalsInstance.getSetting('voice-manager-api.base-url')
DEFAULT_TIMEOUT_IN_SECONDS = globalsInstance.getSetting('voice-manager-api.default-timeout-in-seconds')
API_KEY = globalsInstance.getSetting('voice-manager-api.api-key')
