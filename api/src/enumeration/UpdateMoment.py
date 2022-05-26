from python_framework import Enum, EnumItem


@Enum()
class UpdateMomentEnumeration :
    TODAY_NEWS = EnumItem(**globalsInstance.getSetting('today-news.update'))


UpdateMoment = UpdateMomentEnumeration()
