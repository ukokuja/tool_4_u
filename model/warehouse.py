from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE
from controller import ViewSet
association_table = Table('warehouse_items', T4U_BASE.metadata,
                          Column('warehouse_id', Integer, ForeignKey('warehouse.id')),
                          Column('item_id', Integer, ForeignKey('item.id')),
                          Column('count', Integer)
                          )


class Warehouse(T4U_BASE):
    __tablename__ = 'warehouse'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    location = Column(Integer, ForeignKey('location.id'))
    neighbourhood_id = Column(Integer, ForeignKey('neighbourhood.id'))
    items = relationship("Item", secondary=association_table)
