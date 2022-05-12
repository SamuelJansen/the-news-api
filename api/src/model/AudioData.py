from python_helper import Constant as c
from python_helper import ObjectHelper, DateTimeHelper
from python_framework import SqlAlchemyProxy as sap
from ModelAssociation import AUDIO_DATA, MODEL


class AudioData(MODEL):
    __tablename__ = AUDIO_DATA

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    createdAt = sap.Column(sap.DateTime(), nullable=False)
    key = sap.Column(sap.String(sap.STRING_SIZE), nullable=False)
    date = sap.Column(sap.Date(), nullable=False)
    text = sap.Column(sap.String(sap.GIANT_STRING_SIZE), nullable=False)
    voice = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False)
    extension = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False)
    duration = sap.Column(sap.Float(), nullable=False)
    staticUrl = sap.Column(sap.String(sap.LARGE_STRING_SIZE), nullable=False)

    def __init__(self,
        id = None,
        createdAt = None,
        key = None,
        date = None,
        text = None,
        voice = None,
        extension = None,
        duration = None,
        staticUrl = None
    ):
        self.id = id
        self.createdAt = DateTimeHelper.dateTimeNow() if ObjectHelper.isNone(createdAt) else DateTimeHelper.forcedlyGetDateTime(createdAt)
        self.key = key
        self.date = DateTimeHelper.dateNow() if ObjectHelper.isNone(date) else DateTimeHelper.forcedlyGetDate(date)
        self.text = text
        self.voice = voice
        self.extension = extension
        self.duration = duration
        self.staticUrl = staticUrl

    def __repr__(self):
        return f'{self.__tablename__}(key: {self.key}, date: {self.date}, text: {self.text})'
