from controller.cms.cms import CMS
from controller.events.events import Events
from controller.inventory.inventory import Inventory
from controller.orders.orders import Orders
from controller.users.auth import Auth
from controller.users.user_mgmt import UserMgmt


class ControllerManager(object):
    def __init__(self, model):
        self.auth = Auth(model)
        self.user_mgmt = UserMgmt(model)
        self.orders = Orders(model)
        self.inventory = Inventory(model)
        self.events = Events(model)
        self.cms = CMS(model)
