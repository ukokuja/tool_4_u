from consolemenu import ConsoleMenu

from view.cms_menu import CMSMenu
from view.orders_menu import OrdersMenu
from view.inventory_menu import InventoryMenu
from view.auth_menu import AuthMenu


class ViewManager:
    def __init__(self, controller):
        self._controller = controller
        self._menu = ConsoleMenu("Tool 4 You!", "Why buy if you can rent? :)")
        self.auth_menu = AuthMenu(menu=self._menu, controller=controller)
        self.inventory_menu = InventoryMenu(menu=self._menu, controller=controller)
        self.orders_menu = OrdersMenu(menu=self._menu, controller=controller)
        self.cms_menu = CMSMenu(menu=self._menu, controller=controller)

    def start(self):
        self._menu.show()