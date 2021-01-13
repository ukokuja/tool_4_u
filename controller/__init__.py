from controller.cms.cms import CMS
from controller.events.events import Events
from controller.inventory.inventory import Inventory
from controller.orders.orders import Orders
from controller.users.auth import Auth
from controller.users.user_mgmt import UserMgmt

class ViewSet(object):

    def get(self, id):
        return self._session.query(self._entity).get(id)

    def query(self, **kwargs):
        return self._session.query(self._entity).filter_by(**kwargs).all()

    def list(self):
        self._session.query(self._entity).all()

    def create(self, **kwargs):
        self._session.add(self._entity(**kwargs))

    def update(self, **kwargs):
        self._session.update(self._entity(**kwargs))

    def delete(self, id):
        self._session.delete(self._entity, id=id)


class ControllerManager(object):
    def __init__(self, model):
        self.__model = model
        self.auth = Auth(model)
        self.user_mgmt = UserMgmt(model)
        self.orders = Orders(model)
        self.inventory = Inventory(model)
        self.events = Events(model)
        self.cms = CMS(model)

