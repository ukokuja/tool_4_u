from sqlalchemy import Column, Integer, String, ForeignKey

from database import T4U_BASE
from controller import ViewSet

class Location(T4U_BASE):
    __tablename__ = 'location'
    id = Column(Integer, primary_key=True)
    address_street = Column(String(255))
    address_number = Column(Integer)
    city = Column(Integer, ForeignKey('city.id'))
    latitude = Column(String(255))
    longitude = Column(String(255))
