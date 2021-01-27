from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE

class Location(T4U_BASE):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    address_street = Column(String(255))
    address_number = Column(Integer)
    latitude = Column(String(255))
    longitude = Column(String(255))

    warehouse_id = Column(Integer, ForeignKey('warehouse.id'))
    warehouse = relationship("Warehouse", back_populates="location")


    def __repr__(self):
        return "%s %s" % (self.address_street, self.address_number)