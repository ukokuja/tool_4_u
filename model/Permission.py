from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('left_id', Integer, ForeignKey('left.id')),
                          Column('right_id', Integer, ForeignKey('right.id'))
                          )


class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True)
    allowed_actions = relationship("AllowedAction",
                               secondary=association_table)

