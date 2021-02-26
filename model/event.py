import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE


class Event(T4U_BASE):

    __tablename__ = 'event'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    category = Column(String(255))
    action = Column(String(255))
    label = Column(String(255))
    client_id = Column(Integer, ForeignKey('user.id'))
    client = relationship("Client")

    def __repr__(self):
        return "[%s] %s|%s|%s" % (self.timestamp, self.category, self.action, self.label)

    def get_full_description(self):
        return "Date: %s\nCategory: %s\nAction: %s\nLabel: %s\nClient: %s" % (self.timestamp.strftime("%B %d, %Y"),
                                                                              self.category, self.action, self.label,
                                                                              self.client)