from consolemenu import ConsoleMenu, PromptUtils, Screen
from Observable import Observer
from view.cms_menu import CMSMenu
from view.drawer.client import ClientDrawer
from view.drawer.item import ItemDrawer
from view.drawer.item_list import ItemListDrawer
from view.drawer.list import ListDrawer
from view.drawer.logged_out import LoggedOutDrawer
from view.drawer.order import OrderDrawer
from view.drawer.order_confirmed import OrderConfirmedDrawer
from view.drawer.signed_in import SignedInDrawer
from view.drawer.warehouse import WarehouseDrawer
from view.drawer.warehouses_list import WarehousesListDrawer
from view.orders_menu import OrdersMenu
from view.auth_menu import AuthMenu
from view.search_menu import InventoryMenu


class ViewManager(Observer):
    def __init__(self, controller):
        self._controller = controller
        self._menu = ConsoleMenu("Tool 4 You!", "Why buy if you can rent? :)")
        self.auth_menu = AuthMenu(menu=self._menu, controller=self._controller)
        self.inventory_menu = InventoryMenu(menu=self._menu, controller=self._controller)
        self.orders_menu = OrdersMenu(menu=self._menu, controller=self._controller)
        self.cms_menu = CMSMenu(menu=self._menu, controller=self._controller)
        self.drawer = {
            "list": ListDrawer(controller=self._controller),
            "item": ItemDrawer(controller=self._controller),
            "warehouses": WarehousesListDrawer(controller=self._controller),
            "warehouse": WarehouseDrawer(controller=self._controller),
            "confirm_order": OrderDrawer(controller=self._controller, client={"id": 1}),
            "order": OrderConfirmedDrawer(controller=self._controller),
            "client": ClientDrawer(controller=self._controller),
            "signed_in": SignedInDrawer(controller=self._controller),
            "logged_out": LoggedOutDrawer(controller=self._controller)
        }

    def start(self):
        self._menu.show()

    def update(self, object):
        handler = type(object).__name__.lower()
        while object:
            data_type = type(object).__name__.lower()
            if handler in self.drawer:
                object, handler = self.drawer[handler].draw(object)
            else:
                object, handler = self.drawer[data_type].draw(object)
        self._menu.resume()
