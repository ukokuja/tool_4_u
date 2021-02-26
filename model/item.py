import textwrap

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import T4U_BASE

from model.image import Image
from model.comment import Comment


class Item(T4U_BASE):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(1024))
    images = relationship("Image")
    comments = relationship("Comment")
    warehouses = relationship("WarehouseItems", back_populates="item")

    def __repr__(self):
        count = ""
        if hasattr(self, 'count'):
            count = "{} ordered - ".format(self.__getattribute__('count'))
        return "\033[1m%s\033[0m: %s%s" % (
            self.title, count, (self.description[:40] + '..') if len(self.description) > 40 else self.description)

    def get_full_description(self):
        return "\033[1m%s\033[0m:\n%s\n\n\033[1mComments\033[0m:\n%s" % (
            self.title, textwrap.fill(self.description, width=50), '\n'.join(["* {}\n".format(x.text) for x in self.comments]))
