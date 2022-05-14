from python_helper import Constant as c
from python_helper import log
from python_framework import Service, ServiceMethod


MAX_ATTEMPTS = 3


@Service()
class EmailService:

    @ServiceMethod(requestClass=[int, str, str])
    def getMessages(self, amount, origin, emailBox, attempts=MAX_ATTEMPTS):
        log.status(self.getMessages, f'Getting {amount} "{emailBox}" mail box messages from "{origin}"')
        try:
            messageList = self.client.email.getMessages(
                params = {
                    'amount': amount,
                    'origin': origin,
                    'emailBox': emailBox
                }
            )
        except Exception as exception:
            attempts -= 1
            if 0 == attempts:
                raise exception
            log.failure(self.getMessages, f'Error while getting email messages. Going for the {MAX_ATTEMPTS - attempts + 1}° attempt', exception=exception, muteStackTrace=True)
            return self.getMessages(amount, origin, emailBox, attempts=attempts)
        return messageList
