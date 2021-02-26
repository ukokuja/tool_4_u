from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from controller.viewset import ViewSet
from model.user import User


class Client(User, ViewSet):
    __tablename__ = 'client'
    id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    plan_id = Column(Integer, ForeignKey('plan.id'))
    plan = relationship("Plan", back_populates="client")
    phone_number = Column(String(63))

    __mapper_args__ = {
        'polymorphic_identity': 'client',
        'polymorphic_load': 'selectin',
        'with_polymorphic': '*'
    }

    def __getitem__(self, field):
        """
        Allows subscriptable model
        :param field:
        :return:
        """
        return self.__dict__.get(field, None)
