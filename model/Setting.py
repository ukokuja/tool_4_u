import enum

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

Base = declarative_base()


class DataType(enum.Enum):
    number = Integer
    text = String


class Setting(Base):
    __tablename__ = 'setting'
    id = Column(Integer, primary_key=True)
    key = Column(String)
    value = Column(String)
    data_type = Column(enum.Enum(DataType))

    user_id = Column(Integer, ForeignKey('user.id'))