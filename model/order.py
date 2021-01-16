import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy import ForeignKey

from database import T4U_BASE

class Order(T4U_BASE):

    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('user.id'))
    item_id = Column(Integer, ForeignKey('item.id'))
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'))
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, nullable=True)
