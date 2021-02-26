from consolemenu import ConsoleMenu
from consolemenu.items import SelectionItem


class SelectionActionItem(SelectionItem):

    def __init__(self, text, index, action, menu=None):
        super(SelectionActionItem, self).__init__(text=text, index=index, menu=menu)
        self.action = action

    def action(self):
        self.action()


class SelectionActionMenu(ConsoleMenu):
    def __init__(self, actions, **kwargs):
        self.actions = actions
        super(SelectionActionMenu, self).__init__(**kwargs)
        for index, item in enumerate(self.actions):
            self.append_item(
                SelectionActionItem(text=item.get('title'), action=item.get('action'), index=index, menu=self))


class T4UMenu(ConsoleMenu):
    USER_LOGGED_IN = "is_logged_in"
    USER_IS_MANAGER = "is_manager"
    USER_LOGGED_OUT = "is_logged_out"

    def __init__(self, **kwargs):
        self.__controller = kwargs.pop('user_mgmt_controller')
        super().__init__(**kwargs)
        self.__items = []
        self.exit_item.condition = None

    def append_item(self, item, condition=None):
        item.condition = condition
        self.__items.append(item)

    def draw(self):
        self.items = []
        for item in self.__items:
            if not item.condition or self.__controller[item.condition]():
                super().append_item(item)
        self.add_exit()
        self.screen.printf(self.formatter.format(title=self.title, subtitle=self.subtitle, items=self.items,
                                                 prologue_text=self.prologue_text, epilogue_text=self.epilogue_text))