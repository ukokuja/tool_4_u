from controller.cms.cms import CMS
from controller.events.events import Events
from controller.inventory.inventory import Inventory
from controller.orders.orders import Orders
from controller.users.auth import Auth
from controller.users.user_mgmt import UserMgmt
from controller.utils.utils import Utils


class ControllerManager(object):
    def __init__(self, model):
        self.__client = None

        self.auth = Auth(model)
        self.user_mgmt = UserMgmt(model)
        self.orders = Orders(model)
        self.inventory = Inventory(model)
        self.utils = Utils(model)
        self.events = Events(model)
        self.cms = CMS(model)

    def register_auth(self, client):
        if not self.is_logged_in():
            self.__client = client
            return True
        return False

    def remove_auth(self):
        self.__client = None

    def is_logged_in(self):
        return self.__client is not None

    def is_logged_out(self):
        return not self.is_logged_in()

    def get_client(self):
        return self.__client

    def get_client_prop(self, prop):
        return self.__client[prop]

    def get_user_mgmt_functions(self):
        return {
            "is_logged_in": self.is_logged_in,
            "is_logged_out": self.is_logged_out
        }