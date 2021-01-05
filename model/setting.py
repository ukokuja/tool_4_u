import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import ForeignKey

from database import T4U_BASE
from controller import ViewSet

class DataType(enum.Enum):
    number = Integer
    text = String


class Setting(T4U_BASE):
    __tablename__ = 'setting'
    id = Column(Integer, primary_key=True)
    key = Column(String(255))
    value = Column(String(255))
    data_type = Column(Enum(DataType))

    user_id = Column(Integer, ForeignKey('user.id'))