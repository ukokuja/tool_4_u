from sqlalchemy import Column, Integer, String, ForeignKey

from database import T4U_BASE
from controller import ViewSet

class Comment(T4U_BASE):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(255))
    item_id = Column(Integer, ForeignKey('item.id'))

    def __repr__(self):
        return self.text



