from Observable import Observable
from model.allowed_action import AllowedAction
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
from model.payment_method import PaymentMethod
from model.permission import Permission
from model.role import Role
from model.setting import Setting
from model.user import User
from model.warehouse import Warehouse


class ModelManager(Observable):
    def __init__(self, session):
        self._allowed_action = EntityManager(session, AllowedAction)
        self._audit = EntityManager(session, Audit)
        self._city = EntityManager(session, City)
        self.client = EntityManager(session, Client)
        self._comment = EntityManager(session, Comment)
        self._event = EntityManager(session, Event)
        self._image = EntityManager(session, Image)
        self.item = EntityManager(session, Item)
        self._location = EntityManager(session, Location)
        self._neighbourhood = EntityManager(session, Neighbourhood)
        self.order = EntityManager(session, Order)
        self._payment_method = EntityManager(session, PaymentMethod)
        self._permission = EntityManager(session, Permission)
        self._plan = EntityManager(session, Plan)
        self._role = EntityManager(session, Role)
        self._setting = EntityManager(session, Setting)
        self.user = EntityManager(session, User)
        self._warehouse = EntityManager(session, Warehouse)

