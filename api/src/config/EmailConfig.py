from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()

BASE_URL = globalsInstance.getSetting('email-manager-api.base-url')
DEFAULT_TIMEOUT_IN_SECONDS = globalsInstance.getSetting('email-manager-api.default-timeout-in-seconds')
API_KEY = globalsInstance.getSetting('email-manager-api.api-key')
