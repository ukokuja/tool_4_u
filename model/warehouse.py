from sqlalchemy import Column, Integer, String, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE

class WarehouseItems(T4U_BASE):
    __tablename__ = 'warehouse_items'
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)
    count = Column('count', Integer)
    item = relationship("Item", back_populates="warehouses")
    warehouse = relationship("Warehouse", back_populates="items")

    def get_full_description(self):
        return "hereeee WarehouseItems"

    def __repr__(self):
        return "Warehouse: %s - %s | %s availables" % (self.warehouse.neighbourhood.name, self.warehouse.neighbourhood.city.name, self.count)

class Warehouse(T4U_BASE):
    __tablename__ = 'warehouse'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    items = relationship("WarehouseItems", back_populates="warehouse")
    location = relationship("Location", uselist=False, back_populates="warehouse")

    neighbourhood_id = Column(Integer, ForeignKey('neighbourhood.id'))
    neighbourhood = relationship("Neighbourhood", back_populates="warehouse")

    def get_full_description(self):
        return "" #TODO: Change

    def __repr__(self):
        return "%s in %s" % (self.location, self.neighbourhood)
