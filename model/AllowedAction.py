from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class AllowedAction(Base):
    __tablename__ = 'allowed_action'
    id = Column(Integer, primary_key=True)
    action = Column(String)

