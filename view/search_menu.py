from consolemenu import Screen, PromptUtils
from consolemenu.items import SubmenuItem

from view.base_menu import BaseMenu
from view.console.adaptor import SelectionActionMenu


class InventoryMenu(BaseMenu):
    def __init__(self, menu, controller):
        super().__init__(menu=menu, controller=controller)
        level_1 = SelectionActionMenu(actions=[
            {"title": "Search by title", "action": self.search},
            {"title": "Search by city", "action": self.search_by_city},
        ])
        level_2 = SubmenuItem("Search", level_1, menu)
        self._menu.append_item(level_2)

    def search(self):
        title = self._prompt_utils.input(prompt='Enter title: ', validators=None)
        self._controller.inventory.search(title=title.input_string)

    def search_by_city(self):
        city = self._prompt_utils.prompt_for_numbered_choice(title='Enter city:', choices=["Tel Aviv", "Netania"])
        self._controller.inventory.search_by_city(city=city.input_string)
