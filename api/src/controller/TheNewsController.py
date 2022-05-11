from python_framework import Controller, ControllerMethod, HttpStatus, EnumItemStr


@Controller(url = '/the-news', tag='The News', description='The News controller')
class TheNewsController:

    @ControllerMethod(url='/today'
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.USER]
    )
    def put(self):
        return self.service.theNews.updateTodaysNews(), HttpStatus.OK

    @ControllerMethod(url='/today'
        # apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.USER]
    )
    def get(self):
        return self.service.theNews.getTodaysNewsAudios(), HttpStatus.OK
