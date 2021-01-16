from consolemenu.items import SubmenuItem

from view.base_menu import BaseMenu
from view.console.adaptor import SelectionActionMenu


class HomeMenu(BaseMenu):
    def __init__(self, menu, controller, prompt):
        super().__init__(menu=menu, controller=controller, prompt=prompt)
        level_2 = SelectionActionMenu(actions=[
            {"title": "Search by title", "action": self.search},
            {"title": "Search by city", "action": self.search_by_city},
        ])
        level_1 = SubmenuItem("Search", level_2, menu)
        self._menu.append_item(level_1)

    def search(self):
        title = self._prompt_utils.input(prompt='Enter title: ', validators=None)
        self._controller.inventory.search(title=title.input_string)

    def search_by_city(self):
        city = self._prompt_utils.prompt_for_numbered_choice(title='Enter city:', choices=["Tel Aviv", "Netania"])
        self._controller.inventory.search_by_city(city=city.input_string)
