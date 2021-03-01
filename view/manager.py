from consolemenu import ConsoleMenu, PromptUtils, Screen
from Observable import Observer
from view.analytics_menu import AnalyticsMenu
from view.cms_menu import CMSMenu
from view.console.adaptor import T4UMenu
from view.drawer.active_orders import ActiveOrdersDrawer
from view.drawer.city import CityDrawer
from view.drawer.client import ClientControlDrawer
from view.drawer.cms import AddWarehouseDrawer, AddCityDrawer, AddNeighbourhoodDrawer, AddItemDrawer, EditCityDrawer, \
    EditNeighbourhoodDrawer, EditWarehouseDrawer, EditItemDrawer, RemoveCityDrawer, RemoveNeighbourhoodDrawer, \
    RemoveWarehouseDrawer, RemoveItemDrawer
from view.drawer.confirm_order import ConfirmOrderDrawer

from view.drawer.description import DescriptionControlDrawer
from view.drawer.finish_order_confirm import FinishOrderConfirmControlDrawer
from view.drawer.item import ItemControlDrawer
from view.drawer.list import ListControlDrawer
from view.drawer.list_with_type import ListWithTypeControlDrawer
from view.drawer.logged_out import LoggedOutControlDrawer
from view.drawer.message import MessageDrawer
from view.drawer.order import OrderDrawer
from view.drawer.order_confirmed import OrderConfirmedControlDrawer
from view.drawer.signed_in import SignedInControlDrawer
from view.drawer.user_active_orders import UserActiveOrdersDrawer
from view.drawer.warehouse import WarehouseControlDrawer
from view.drawer.warehouses_list import WarehousesListDrawer
from view.orders_menu import OrdersMenu
from view.auth_menu import AuthMenu
from view.search_menu import InventoryMenu
from view.user_mgmt_menu import UserMgmtMenu

SUBTITLE = "why buy if you can rent? :)"
TITLE = "Tool 4 You!"


class ViewManager(Observer):
    def __init__(self, controller):
        self._controller = controller
        self._menu = T4UMenu(title=TITLE.capitalize(), subtitle=SUBTITLE.capitalize(),
                             user_mgmt_controller=controller.get_user_mgmt_functions())
        self.inventory_menu = InventoryMenu(menu=self._menu, controller=self._controller)
        self.orders_menu = OrdersMenu(menu=self._menu, controller=self._controller)
        self.user_mgmt_menu = UserMgmtMenu(menu=self._menu, controller=self._controller)
        self.cms_menu = CMSMenu(menu=self._menu, controller=self._controller)
        self.analytics_menu = AnalyticsMenu(menu=self._menu, controller=self._controller)
        self.auth_menu = AuthMenu(menu=self._menu, controller=self._controller)

        self.drawer = {
            "list": ListControlDrawer(controller=self._controller),
            "search_results_by_title": ListControlDrawer(controller=self._controller),
            "search_results_by_city": ListControlDrawer(controller=self._controller),
            "item": ItemControlDrawer(controller=self._controller),
            "most_ordered_items": ListWithTypeControlDrawer(controller=self._controller, type="user_items"),
            "user_items": DescriptionControlDrawer(controller=self._controller),
            "order": OrderDrawer(controller=self._controller),
            "cities": ListControlDrawer(controller=self._controller),
            "city": CityDrawer(controller=self._controller),
            "event": DescriptionControlDrawer(controller=self._controller),
            "warehouses": WarehousesListDrawer(controller=self._controller),
            "warehouse": WarehouseControlDrawer(controller=self._controller),
            "confirm_order": ConfirmOrderDrawer(controller=self._controller),
            "order_created": OrderConfirmedControlDrawer(controller=self._controller),
            "sign_up": ClientControlDrawer(controller=self._controller),
            "sign_in": SignedInControlDrawer(controller=self._controller),
            "sign_out": MessageDrawer(message="Logged out"),
            "user_updated": MessageDrawer(message="User updated"),
            "logged_out": LoggedOutControlDrawer(controller=self._controller),
            "show_active_orders": ActiveOrdersDrawer(controller=self._controller,
                                                     title="Please choose an order to finish"),
            "show_user_active_orders": UserActiveOrdersDrawer(controller=self._controller,
                                                     title="Choose an order to see the description"),
            "finish_order": FinishOrderConfirmControlDrawer(controller=self._controller),
            "wrong_password": MessageDrawer(message="Wrong password, try again."),

            "add_city": AddCityDrawer(controller=self._controller),
            "add_neighbourhood": AddNeighbourhoodDrawer(controller=self._controller),
            "add_warehouse": AddWarehouseDrawer(controller=self._controller),
            "add_item": AddItemDrawer(controller=self._controller),
            "edit_city": EditCityDrawer(controller=self._controller),
            "edit_neighbourhood": EditNeighbourhoodDrawer(controller=self._controller),
            "edit_warehouse": EditWarehouseDrawer(controller=self._controller),
            "edit_item": EditItemDrawer(controller=self._controller),
            "remove_city": RemoveCityDrawer(controller=self._controller),
            "remove_neighbourhood": RemoveNeighbourhoodDrawer(controller=self._controller),
            "remove_warehouse": RemoveWarehouseDrawer(controller=self._controller),
            "remove_item": RemoveItemDrawer(controller=self._controller),


            "cities_to_add": ListControlDrawer(controller=self._controller),
            "neighbourhood_to_add": ListControlDrawer(controller=self._controller),
            "warehouse_to_add": ListControlDrawer(controller=self._controller),
            "item_to_add": ListControlDrawer(controller=self._controller),
            "cities_to_edit": ListControlDrawer(controller=self._controller),
            "neighbourhood_to_edit": ListControlDrawer(controller=self._controller),
            "warehouse_to_edit": ListControlDrawer(controller=self._controller),
            "item_to_edit": ListControlDrawer(controller=self._controller),
            "cities_to_remove": ListControlDrawer(controller=self._controller),
            "neighbourhood_to_remove": ListControlDrawer(controller=self._controller),
            "warehouse_to_remove": ListControlDrawer(controller=self._controller),
            "item_to_remove": ListControlDrawer(controller=self._controller),

            "city_created": MessageDrawer(message="City created"),
            "neighbourhood_created": MessageDrawer(message="Neighbourhood created"),
            "warehouse_created": MessageDrawer(message="Warehouse created"),
            "item_created": MessageDrawer(message="Item created"),
            "track_user": ListControlDrawer(controller=self._controller),

            "update user first name": MessageDrawer(message="First name was changed"),
            "update user last name": MessageDrawer(message="Last name was changed"),
            "update user phone number": MessageDrawer(message="Phone number was changed"),
            "update user email": MessageDrawer(message="Email was changed"),

            "return tool": MessageDrawer(message="Tool was returned"),

        }
        self.__client = None

    def start(self):
        self._menu.show()

    def update(self, object, label):
        handler = label
        while object:
            self._set_name_on_subtitle()
            if handler in self.drawer:
                object, handler = self.drawer[handler].draw(object)
            elif label in self.drawer:
                object, handler = self.drawer[label].draw(object)
            else:
                object, handler = self.drawer[type(object).__name__.lower()].draw(object)
            label = None
            event_label = self._get_event_label(handler, label)
            self._send_event(event_label)
        else:
            if handler:
                self.drawer[handler].draw(object)
        self._set_name_on_subtitle()
        self._menu.resume()

    def _get_event_label(self, handler, label):
        return handler or label or self._menu.selected_item.text

    def _set_name_on_subtitle(self):
        if self._controller.is_logged_in():
            self.__client = self._controller.get_client()
            self._menu.subtitle = "{}, {}".format(self.__client.first_name, SUBTITLE)
        else:
            self._menu.subtitle = SUBTITLE.capitalize()

    def _send_event(self, event_label):
        self._controller.events.send_event(
            category="View",
            action="interaction",
            label=event_label,
            client_id=self._controller.get_client_id())
