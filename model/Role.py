from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

association_table = Table('association', Base.metadata,
                          Column('left_id', Integer, ForeignKey('left.id')),
                          Column('right_id', Integer, ForeignKey('right.id'))
                          )


class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    permissions = relationship("Permission",
                               secondary=association_table)

