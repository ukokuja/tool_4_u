from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import T4U_BASE
from controller import ViewSet
from model.image import Image
from model.comment import Comment

class Item(T4U_BASE):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(1024))
    images = relationship("Image")
    comments = relationship("Comment")

    def __repr__(self):
        return "<Item(id='%s', title='%s', description='%s')>" % (
            self.id, self.title, self.description)


class ItemManager(ViewSet):

    def __init__(self, session, entity):
        self._session = session
        self._entity = entity