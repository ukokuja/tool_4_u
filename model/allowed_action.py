from sqlalchemy import Column, Integer, String

from controller import ViewSet
from database import T4U_BASE


class AllowedAction(T4U_BASE):
    __tablename__ = 'allowed_action'
    id = Column(Integer, primary_key=True)
    action = Column(String(255))



