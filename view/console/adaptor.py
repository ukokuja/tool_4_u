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