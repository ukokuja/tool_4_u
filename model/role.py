from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Table, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE
from controller import ViewSet

association_table = Table('role_permission', T4U_BASE.metadata,
                          Column('role_id', Integer, ForeignKey('role.id')),
                          Column('permission_id', Integer, ForeignKey('permission.id'))
                          )


class Role(T4U_BASE):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    permissions = relationship("Permission",
                               secondary=association_table)

