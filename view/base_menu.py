from consolemenu import PromptUtils, Screen


class BaseMenu(object):
    def __init__(self, menu, controller):
        self._menu = menu
        self._controller = controller
        self._prompt_utils = PromptUtils(Screen())