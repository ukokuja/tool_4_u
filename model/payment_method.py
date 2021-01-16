from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE

class PaymentMethod(T4U_BASE):
    __tablename__ = 'payment_method'
    id = Column(Integer, primary_key=True)
    name = Column(String(63))
    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="payment_method")