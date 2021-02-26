from Observable import Observable
from model.audit import Audit
from model.city import City
from model.client import Client
from model.plan import Plan
from model.comment import Comment
from model.entity_manager import EntityManager
from model.event import Event
from model.image import Image
from model.item import Item
from model.location import Location
from model.neighbourhood import Neighbourhood
from model.order import Order
from model.role import Role
from model.setting import Setting
from model.user import User
from model.warehouse import Warehouse, WarehouseItems


class ModelManager(Observable):
    def __init__(self, session):
        self._audit = EntityManager(session, Audit)
        self.city = EntityManager(session, City)
        self.client = EntityManager(session, Client)
        self._comment = EntityManager(session, Comment)
        self.event = EntityManager(session, Event)
        self._image = EntityManager(session, Image)
        self.item = EntityManager(session, Item)
        self.location = EntityManager(session, Location)
        self.neighbourhood = EntityManager(session, Neighbourhood)
        self.order = EntityManager(session, Order)
        self.plan = EntityManager(session, Plan)
        self.role = EntityManager(session, Role)
        self._setting = EntityManager(session, Setting)
        self.user = EntityManager(session, User)
        self.warehouse = EntityManager(session, Warehouse)
        self.warehouse_items = EntityManager(session, WarehouseItems)

