from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from model.user import User

Base = declarative_base(cls=User)
from controller import ViewSet

class Client(Base, ViewSet):
    __tablename__ = 'client'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    plan = relationship("Plan")
    phone_number = Column(String(63))
    payment_method = relationship("PaymentMethod", uselist=False, back_populates="client")

    __mapper_args__ = {
        'polymorphic_identity': 'client',
    }