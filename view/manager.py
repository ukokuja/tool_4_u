from consolemenu import ConsoleMenu
from Observable import Observer
from view.cms_menu import CMSMenu
from view.orders_menu import OrdersMenu
from view.inventory_menu import InventoryMenu
from view.auth_menu import AuthMenu
from sqlalchemy import inspect


class BaseDrawer():

    @staticmethod
    def draw(instance):
        inspected_instance = inspect(instance)
        for key in inspected_instance.mapper.column_attrs.keys():
            print("{}: {}".format(key, inspected_instance.dict[key]))


class ItemDrawer(BaseDrawer):
    pass


class ViewManager(Observer):
    def __init__(self, controller):
        self._controller = controller
        self._menu = ConsoleMenu("Tool 4 You!", "Why buy if you can rent? :)")
        self.auth_menu = AuthMenu(menu=self._menu, controller=controller)
        self.inventory_menu = InventoryMenu(menu=self._menu, controller=controller)
        self.orders_menu = OrdersMenu(menu=self._menu, controller=controller)
        self.cms_menu = CMSMenu(menu=self._menu, controller=controller)

        self.drawer = {
            "Item": ItemDrawer
        }

    def start(self):
        self._menu.show()

    def draw(self, object):
        self.drawer[type(object).__name__].draw(object)

    def update(self, objects):
        for object in objects:
            self.draw(object)
            self._menu.resume()
