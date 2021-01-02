from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    role_id = Column(Integer, ForeignKey('role.id'))
    settings = relationship("Setting")

    def __repr__(self):
        return "<User(id='%s', fullname='%s %s')>" % (
            self.id, self.first_name, self.last_name)
