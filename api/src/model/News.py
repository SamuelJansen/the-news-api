from python_helper import Constant as c
from python_helper import ObjectHelper, DateTimeHelper
from python_framework import SqlAlchemyProxy as sap
from python_framework import ConverterStatic

from ModelAssociation import NEWS, MODEL
from constant import NewsConstant
from enumeration.NewsStatus import NewsStatus


class News(MODEL):
    __tablename__ = NEWS

    id = sap.Column(sap.Integer(), sap.Sequence(f'{__tablename__}{sap.ID}{sap.SEQ}'), primary_key=True)
    key = sap.Column(sap.String(sap.STRING_SIZE), unique=True, nullable=False)
    date = sap.Column(sap.Date(), nullable=False)
    status = sap.Column(sap.String(sap.LITTLE_STRING_SIZE), nullable=False)
    createdAt = sap.Column(sap.DateTime(), nullable=False)
    updatedAt = sap.Column(sap.DateTime(), nullable=False)

    def __init__(self,
        id = None,
        key = None,
        date = None,
        status = None,
        createdAt = None,
        updatedAt = None
    ):
        self.id = id
        self.key = key
        self.date = date
        self.status = NewsStatus.map(ConverterStatic.getValueOrDefault(status, NewsConstant.DEFAULT_STATUS))
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        ConverterStatic.overrideDateData(self)

    def __repr__(self):
        return f'{self.__tablename__}(key: {self.key}, status: {self.status})'
