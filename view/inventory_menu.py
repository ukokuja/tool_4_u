from consolemenu.items import FunctionItem

from view.base_menu import BaseMenu


class InventoryMenu(BaseMenu):
    def __init__(self, menu, controller):
        super().__init__(menu=menu, controller=controller)
        options = [
            FunctionItem("Search by title", self.search),
        ]
        for options in options:
            self._menu.append_item(options)


    def search(self):
        query = self._prompt_utils.input(prompt='Enter title: ', validators=None)
        self._controller.inventory.search(query=query.input_string)

