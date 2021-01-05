from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE
from controller import ViewSet

class Neighbourhood(T4U_BASE):

    __tablename__ = 'neighbourhood'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    city_id = Column(Integer, ForeignKey('city.id'))
