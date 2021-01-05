from sqlalchemy import Column, Integer, String

from controller import ViewSet
from database import T4U_BASE


class Audit(T4U_BASE):

    __tablename__ = 'audit'
    id = Column(Integer, primary_key=True)
    action = Column(String(255))
    extra_data = Column(String(255))
