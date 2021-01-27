from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE

class Neighbourhood(T4U_BASE):

    __tablename__ = 'neighbourhood'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    warehouse = relationship("Warehouse", back_populates="neighbourhood")


    city_id = Column(Integer, ForeignKey('city.id'))
    city = relationship("City", back_populates="neighbourhood")


    def __repr__(self):
        return "%s, %s" % (self.name, self.city)