from python_framework import Enum, EnumItem


@Enum()
class UpdateMomentEnumeration :
    THE_NEWS = EnumItem(hour=8, minute=30)


UpdateMoment = UpdateMomentEnumeration()
