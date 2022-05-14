from python_framework import Controller, ControllerMethod, HttpStatus, EnumItemStr


@Controller(url = '/the-news', tag='The News', description='The News controller'
    # , logRequest = True
    # , logResponse = True
)
class TheNewsController:

    @ControllerMethod(url='/today'
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.USER]
    )
    def put(self):
        return self.service.theNews.startTodaysNewsUpdate(), HttpStatus.OK

    @ControllerMethod(url='/today'
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.USER]
        # , logRequest = True
        # , logResponse = True
    )
    def get(self):
        return self.service.theNews.getTodaysNewsAudios(), HttpStatus.OK
