from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE

class Plan(T4U_BASE):
    __tablename__ = 'plan'
    id = Column(Integer, primary_key=True)
    price_per_month = Column(Integer)
    allowed_items_per_month = Column(Integer)
    client = relationship("Client")