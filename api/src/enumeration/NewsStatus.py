from python_framework import Enum, EnumItem
from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


@Enum()
class NewsStatusEnumeration:
    CREATED = EnumItem()
    PROCESSING = EnumItem()
    PROCESSING_TEXT = EnumItem()
    PROCESSING_AUDIO = EnumItem()
    FINISHED = EnumItem()
    ERROR = EnumItem()
    NONE = EnumItem()


NewsStatus = NewsStatusEnumeration()
