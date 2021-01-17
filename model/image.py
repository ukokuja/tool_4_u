from sqlalchemy import Column, Integer, String, ForeignKey

from database import T4U_BASE


class Image(T4U_BASE):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    url = Column(String(255))
    item_id = Column(Integer, ForeignKey('item.id'))



