from sqlalchemy import Column, Integer, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE
from controller import ViewSet

association_table = Table('permission_allowed_action', T4U_BASE.metadata,
                          Column('permission_id', Integer, ForeignKey('permission.id')),
                          Column('allowed_action_id', Integer, ForeignKey('allowed_action.id'))
                          )


class Permission(T4U_BASE):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True)
    allowed_actions = relationship("AllowedAction",
                               secondary=association_table)

