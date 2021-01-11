from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE
from controller import ViewSet

class Order(T4U_BASE):

    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('user.id'))
    order_id = Column(Integer, ForeignKey('order.id'))
    start_date = Column(DateTime)
    end_date = Column(DateTime, nullable=True)
