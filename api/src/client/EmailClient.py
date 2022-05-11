import webbrowser
from python_helper import log
from python_framework import HttpClient, HttpClientMethod

from config import EmailConfig


@HttpClient(
    url = EmailConfig.BASE_URL,
    timeout = EmailConfig.DEFAULT_TIMEOUT_IN_SECONDS,
    headers = {
        'Api-Key': f'Bearer {EmailConfig.API_KEY}'
    }
    , logRequest = True
    , logResponse = True
)
class EmailClient:

    @HttpClientMethod(
        url = '/content',
        requestParamClass = [dict]
        , logRequest = True
        , logResponse = True
    )
    def getMessages(self, params=None):
        return self.get(params=params)
