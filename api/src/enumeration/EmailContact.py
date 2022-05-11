from python_framework import Enum, EnumItem
from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


@Enum()
class EmailContactEnumeration :
    THE_NEWS = EnumItem(email=globalsInstance.getSetting('email-manager-api.contacts.the-news'))


EmailContact = EmailContactEnumeration()
