from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE


class City(T4U_BASE):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    country = Column(String(255))

    neighbourhood = relationship("Neighbourhood", back_populates="city")

    def __repr__(self):
        return "%s, %s" % (self.name, self.country)