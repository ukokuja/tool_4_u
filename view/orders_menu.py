from consolemenu import Screen, PromptUtils
from consolemenu.items import SubmenuItem

from view.base_menu import BaseMenu
from view.console.adaptor import SelectionActionMenu, T4UMenu


class OrdersMenu(BaseMenu):
    def __init__(self, menu, controller):
        super().__init__(menu=menu, controller=controller)
        level_1 = SelectionActionMenu(actions=[
            {"title": "Return item", "action": self.show_active_orders},
            {"title": "Show active orders", "action": self.show_active_orders},
            {"title": "Show expired orders", "action": self.show_expired_orders},
            {"title": "Show all orders", "action": self.show_orders},
        ])
        level_2 = SubmenuItem("My orders", level_1, menu)
        self._menu.append_item(level_2, T4UMenu.USER_LOGGED_IN)


    def show_active_orders(self):
        client = self._controller.get_client()
        self._controller.orders.show_active_orders(client_id=client.id)

    def show_expired_orders(self):
        client = self._controller.get_client()
        self._controller.orders.show_expired_orders(client_id=client.id)

    def show_orders(self):
        client = self._controller.get_client()
        self._controller.orders.show_orders(client_id=client.id)

