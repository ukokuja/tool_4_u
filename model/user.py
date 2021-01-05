from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE
from controller import ViewSet

class User(T4U_BASE):

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    role_id = Column(Integer, ForeignKey('role.id'))
    settings = relationship("Setting")

    __mapper_args__ = {
        'polymorphic_identity': 'user'
    }

    def __repr__(self):
        return "<User(id='%s', fullname='%s %s')>" % (
            self.id, self.first_name, self.last_name)
