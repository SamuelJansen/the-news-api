from python_helper import Constant as c
from python_helper import ObjectHelper, DateTimeHelper


class AudioDataRequestDto:

    def __init__(self,
        key = None,
        date = None,
        text = None,
        voice = None,
        extension = None,
        duration = None,
        staticUrl = None
    ):
        self.key = key
        self.date = date
        self.text = text
        self.voice = voice
        self.extension = extension
        self.duration = duration
        self.staticUrl = staticUrl


class AudioDataResponseDto:

    def __init__(self,
        key = None,
        date = None,
        text = None,
        voice = None,
        extension = None,
        duration = None,
        staticUrl = None
    ):
        self.key = key
        self.date = date
        self.text = text
        self.voice = voice
        self.extension = extension
        self.duration = duration
        self.staticUrl = staticUrl
