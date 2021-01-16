from consolemenu import ConsoleMenu
from consolemenu.items import SelectionItem


class SelectionActionItem(SelectionItem):

    def __init__(self, text, index, action, menu=None):
        super(SelectionActionItem, self).__init__(text=text, index=index, menu=menu)
        self.action = action

    def action(self):
        self.action()


class SelectionActionMenu(ConsoleMenu):
    def __init__(self, actions, title=None, subtitle=None, screen=None, formatter=None,
                 prologue_text=None, epilogue_text=None, show_exit_option=True, exit_option_text='Exit'):
        self.actions = actions
        super(SelectionActionMenu, self).__init__(title=title, subtitle=subtitle, screen=screen, formatter=formatter,
                                                  prologue_text=prologue_text, epilogue_text=epilogue_text,
                                                  show_exit_option=show_exit_option, exit_option_text=exit_option_text)
        for index, item in enumerate(self.actions):
            self.append_item(
                SelectionActionItem(text=item.get('title'), action=item.get('action'), index=index, menu=self))