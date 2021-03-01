from consolemenu import SelectionMenu
from consolemenu.items import SubmenuItem

from view.base_menu import BaseMenu
from view.console.adaptor import SelectionActionMenu, T4UMenu


class CMSMenu(BaseMenu):
    def __init__(self, menu, controller):
        super().__init__(menu=menu, controller=controller)
        level_1 = SelectionActionMenu(actions=[
            {"title": "Add city", "action": self.add_city},
            {"title": "Edit city", "action": self.edit_city},
            {"title": "Add neighbourhood", "action": self.add_neighbourhood},
            {"title": "Edit neighbourhood", "action": self.edit_neighbourhood},
            {"title": "Add warehouse", "action": self.add_warehouse},
            {"title": "Edit warehouse", "action": self.edit_warehouse},
            {"title": "Add item", "action": self.add_item},
            {"title": "Edit item", "action": self.edit_item},
            {"title": "Remove item", "action": self.remove_item},
        ])
        level_2 = SubmenuItem("Content manager", level_1, menu)
        self._menu.append_item(level_2, T4UMenu.USER_IS_MANAGER)

    def add_city(self):
        country = self._prompt_utils.input(prompt='Country')
        name = self._prompt_utils.input(prompt='Name')
        self._controller.cms.add_city(country=country.input_string, name=name.input_string)

    def add_neighbourhood(self):
        cities = self._controller.cms.add_neighbourhood()
        name = self._prompt_utils.input(prompt='Name')
        options = SelectionMenu(title="Choose a city",
                                exit_option_text="Return to Tool 4 You!",
                                strings=cities)
        options.show()
        if not options.is_selected_item_exit():
            self._controller.cms.add_neighbourhood(name.input_string, city_id=options.selected_item.text.id)

    def add_warehouse(self):
        name = self._prompt_utils.input(prompt='Name')
        address_street = self._prompt_utils.input(prompt='Address street')
        address_number = self._prompt_utils.input(prompt='Address number')
        neighbourhoods = self._controller.cms.add_warehouse()
        options = SelectionMenu(title="Choose a neighbourhood",
                                exit_option_text="Return to Tool 4 You!",
                                strings=neighbourhoods)
        options.show()
        if not options.is_selected_item_exit():
            self._controller.cms.add_warehouse(address_street=address_street.input_string,
                                               address_number=address_number.input_string,
                                               name=name.input_string,
                                               neighbourhood_id=options.selected_item.text.id
                                               )

    def add_item(self):
        title = self._prompt_utils.input(prompt='Title')
        description = self._prompt_utils.input(prompt='Description')
        count = self._prompt_utils.input(prompt='Count')
        warehouses = self._controller.cms.add_item()
        options = SelectionMenu(title="Choose a warehouse",
                                exit_option_text="Return to Tool 4 You!",
                                strings=warehouses)
        options.show()
        if not options.is_selected_item_exit():
            self._controller.cms.add_item(title=title.input_string, description=description.input_string,
                                          warehouse_id=options.selected_item.text.id, count=count.input_string)

    def edit_city(self):
        cities = self._controller.cms.edit_city()
        options = SelectionMenu(title="Choose a city",
                                exit_option_text="Return to Tool 4 You!",
                                strings=cities)
        options.show()
        if not options.is_selected_item_exit():
            country = self._prompt_utils.input(prompt='Country', default=options.selected_item.text.country)
            name = self._prompt_utils.input(prompt='Name', default=options.selected_item.text.name)
            self._controller.cms.edit_city(name=name.input_string, city_id=options.selected_item.text.id,
                                           country=country.input_string)

    def remove_city(self):
        cities = self._controller.cms.remove_city()
        options = SelectionMenu(title="Choose a city",
                                exit_option_text="Return to Tool 4 You!",
                                strings=cities)
        options.show()
        if not options.is_selected_item_exit():
            self._controller.cms.remove_city(city_id=options.selected_item.text.id)

    def edit_neighbourhood(self):
        neighbourhoods = self._controller.cms.edit_neighbourhood()
        options = SelectionMenu(title="Choose a Neighbourhood",
                                exit_option_text="Return to Tool 4 You!",
                                strings=neighbourhoods)
        options.show()
        if not options.is_selected_item_exit():
            name = self._prompt_utils.input(prompt='Name')
            self._controller.cms.edit_neighbourhood(name=name.input_string, neighbourhood_id=options.selected_item.text.id)

    def remove_neighbourhood(self):
        neighbourhoods = self._controller.cms.remove_neighbourhood()
        options = SelectionMenu(title="Choose a Neighbourhood",
                                exit_option_text="Return to Tool 4 You!",
                                strings=neighbourhoods)
        options.show()
        if not options.is_selected_item_exit():
            self._controller.cms.remove_neighbourhood(neighbourhood_id=options.selected_item.text.id)

    def edit_warehouse(self):
        warehouses = self._controller.cms.edit_warehouse()
        options = SelectionMenu(title="Choose a Warehouse",
                                exit_option_text="Return to Tool 4 You!",
                                strings=warehouses)
        options.show()
        if not options.is_selected_item_exit():
            name = self._prompt_utils.input(prompt='Name')
            self._controller.cms.edit_warehouse(name=name.input_string, warehouse_id=options.selected_item.text.id)

    def remove_warehouse(self):
        warehouses = self._controller.cms.remove_warehouse()
        options = SelectionMenu(title="Choose a Warehouse",
                                exit_option_text="Return to Tool 4 You!",
                                strings=warehouses)
        options.show()
        if not options.is_selected_item_exit():
            self._controller.cms.remove_warehouse(warehouse_id=options.selected_item.text.id)

    def edit_item(self):

        items = self._controller.cms.edit_item()
        options = SelectionMenu(title="Choose an Item",
                                exit_option_text="Return to Tool 4 You!",
                                strings=items)
        options.show()
        if not options.is_selected_item_exit():
            title = self._prompt_utils.input(prompt='Title')
            description = self._prompt_utils.input(prompt='Description')

            self._controller.cms.edit_item(title=title.input_string, description=description.input_string,
                                           item_id=options.selected_item.text.id)

    def remove_item(self):
        items = self._controller.cms.remove_item()
        options = SelectionMenu(title="Choose an Item",
                                exit_option_text="Return to Tool 4 You!",
                                strings=items)
        options.show()
        if not options.is_selected_item_exit():
            self._controller.cms.remove_item(item_id=options.selected_item.text.id)
