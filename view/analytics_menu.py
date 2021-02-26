from consolemenu import SelectionMenu
from consolemenu.items import SubmenuItem

from view.base_menu import BaseMenu
from view.console.adaptor import SelectionActionMenu, T4UMenu


class AnalyticsMenu(BaseMenu):
    def __init__(self, menu, controller):
        super().__init__(menu=menu, controller=controller)
        level_1 = SelectionActionMenu(actions=[
            {"title": "Most ordered items", "action": self.most_ordered_items},
            {"title": "Unreturned item", "action": self.unreturned_items},
            {"title": "Track user actions", "action": self.track_user},
        ])
        level_2 = SubmenuItem("Analytics", level_1, menu)
        self._menu.append_item(level_2, T4UMenu.USER_IS_MANAGER)

    def most_ordered_items(self):
        self._controller.events.most_ordered_items()

    def unreturned_items(self):
        self._controller.events.unreturned_items()


    def track_user(self):
        users = self._controller.events.track_user()
        options = SelectionMenu(title="Choose a user",
                                exit_option_text="Return to Tool 4 You!",
                                strings=users)
        options.show()
        self._controller.events.track_user(user_id=options.selected_item.text.id)