from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from model.User import User

Base = declarative_base()


class Client(User):

    __tablename__ = 'client'
    plan = relationship("Plan")
    phone_number = Column(String)
    payment_method = relationship("PaymentMethod", uselist=False, back_populates="client")
