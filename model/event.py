import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey

from database import T4U_BASE


class Event(T4U_BASE):

    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    category = Column(String(255))
    action = Column(String(255))
    label = Column(String(255))
    client_id = Column(Integer, ForeignKey('user.id'))