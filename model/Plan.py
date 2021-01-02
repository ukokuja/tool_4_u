from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey

Base = declarative_base()


class Plan(Base):
    __tablename__ = 'plan'
    id = Column(Integer, primary_key=True)
    price_per_month = Column(Integer)
    allowed_items_per_month = Column(Integer)
    client_id = Column(Integer, ForeignKey('client.id'))