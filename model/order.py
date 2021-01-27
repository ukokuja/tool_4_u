import datetime

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from database import T4U_BASE


class Order(T4U_BASE):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('user.id'))
    client = relationship("Client")
    item_id = Column(Integer, ForeignKey('item.id'))
    item = relationship("Item")
    warehouse_id = Column(Integer, ForeignKey('warehouse.id'))
    warehouse = relationship("Warehouse")
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

    def __repr__(self):
        if self.end_date:
            return "%s @ %s finished at %s" % (self.item.title, self.warehouse.location, self.format_end_date())
        return "%s @ %s - from %s" % (self.item.title, self.warehouse.location, self.format_start_date())

    def format_start_date(self):
        return self.start_date.strftime("%B %d, %Y")

    def format_end_date(self):
        return self.end_date.strftime("%B %d, %Y")

    def get_full_description(self):
        if self.end_date:
            return "%s\nOrdered from: %s\nOrdered on: %s\nReturned on: %s" % (self.item.get_full_description(), self.warehouse, self.format_start_date(), self.format_end_date())
        return "%s\nOrdered from:%s\nOrdered on: %s" % (
        self.item.get_full_description(), self.warehouse, self.format_start_date())
