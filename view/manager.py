from consolemenu import ConsoleMenu, PromptUtils, Screen
from Observable import Observer
from view.cms_menu import CMSMenu
from view.drawer.active_orders import ActiveOrdersDrawer
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

SUBTITLE = "why buy if you can rent? :)"
TITLE = "Tool 4 You!"


class ViewManager(Observer):
    def __init__(self, controller):
        self._controller = controller
        self._menu = ConsoleMenu(TITLE.capitalize(), SUBTITLE.capitalize())
        self.auth_menu = AuthMenu(menu=self._menu, controller=self._controller)
        self.inventory_menu = InventoryMenu(menu=self._menu, controller=self._controller)
        self.orders_menu = OrdersMenu(menu=self._menu, controller=self._controller)
        self.cms_menu = CMSMenu(menu=self._menu, controller=self._controller)
        self.drawer = {
            "list": ListDrawer(controller=self._controller),
            "search_results_by_title": ItemDrawer(controller=self._controller),
            "search_results_by_city": ItemDrawer(controller=self._controller),
            # "cities": CityDrawer(controller=self._controller),
            "warehouses": WarehousesListDrawer(controller=self._controller),
            "warehouse": WarehouseDrawer(controller=self._controller),
            "confirm_order": OrderDrawer(controller=self._controller),
            "order_created": OrderConfirmedDrawer(controller=self._controller),
            "sign_up": ClientDrawer(controller=self._controller),
            "sign_in": SignedInDrawer(controller=self._controller),
            "logged_out": LoggedOutDrawer(controller=self._controller),
            "show_active_orders": ActiveOrdersDrawer(controller=self._controller,
                                                     title="Please choose an order to finish"),
        }
        self.__client = None

    def start(self):
        self._menu.show()

    def update(self, object, label):
        handler = label
        while object:
            if handler in self.drawer:
                object, handler = self.drawer[handler].draw(object)
            else:
                object, handler = self.drawer[label].draw(object)
        if self._controller.is_logged_in():
            self.__client = self._controller.get_client()
            self._menu.subtitle = "{}, {}".format(self.__client.first_name, SUBTITLE)
        self._menu.resume()
