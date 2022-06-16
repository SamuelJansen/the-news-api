from python_helper import Constant as c
from python_helper import log
from python_framework import Service, ServiceMethod
from notification_manager_api import NotificationDestiny


MAX_ATTEMPTS = 3


@Service()
class EmailService:

    @ServiceMethod(requestClass=[int, str, str])
    def getMessages(self, amount, origin, emailBox, attempts=MAX_ATTEMPTS):
        logMessage = f'Getting {amount} "{emailBox}" mail box messages from "{origin}"'
        self.service.notification.notifyDebugTo(logMessage, [NotificationDestiny.TELEGRAM])
        log.status(self.getMessages, logMessage)
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
            errorMessage = f'Error while getting email messages. Going for the {MAX_ATTEMPTS - attempts + 1}° attempt'
            log.warning(self.getMessages, errorMessage, exception=exception, muteStackTrace=True)
            self.service.notification.notifyWarningTo(errorMessage, [NotificationDestiny.TELEGRAM])
            return self.getMessages(amount, origin, emailBox, attempts=attempts)
        return messageList
