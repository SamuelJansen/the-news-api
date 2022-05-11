from python_helper import Constant as c
from python_helper import log
from python_framework import Service, ServiceMethod


@Service()
class EmailService:

    @ServiceMethod(requestClass=[int, str, str])
    def getMessages(self, amount, origin, emailBox):
        log.status(self.getMessages, f'Getting {amount} "{emailBox}" mail box messages from "{origin}"')
        messageList = self.client.email.getMessages(
            params = {
                'amount': amount,
                'origin': origin,
                'emailBox': emailBox
            }
        )
        return messageList
