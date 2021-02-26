from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Table, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE

class Role(T4U_BASE):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))


    def __repr__(self):
        return self.name