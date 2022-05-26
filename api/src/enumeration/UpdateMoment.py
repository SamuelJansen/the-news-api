from globals import getGlobalsInstance

from python_framework import Enum, EnumItem


globalsInstance = getGlobalsInstance()


@Enum()
class UpdateMomentEnumeration :
    TODAY_NEWS = EnumItem(**globalsInstance.getSetting('today-news.update'))


UpdateMoment = UpdateMomentEnumeration()
