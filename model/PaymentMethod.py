from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class PaymentMethod(Base):
    __tablename__ = 'payment_method'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="payment_method")