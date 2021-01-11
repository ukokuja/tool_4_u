from consolemenu.items import FunctionItem

from view.base_menu import BaseMenu


class AuthMenu(BaseMenu):

    def sign_up(self):
        username = self._prompt_utils.input(prompt='Username', validators=None)
        full_name = self._prompt_utils.input(prompt='Full name', validators=None)
        password = self._prompt_utils.input_password(message='Password')
        self._controller.auth.sign_up(self=self._controller, username=username.input_string, full_name=full_name.input_string, password=password)

    def sign_in(self):
        username = self._prompt_utils.input(prompt='Username', validators=None)
        password = self._prompt_utils.input_password(message='Password')
        self._controller.auth.sign_in(self=self._controller, username=username.input_string, password=password.input_string)

    def __init__(self, menu, controller):
        super().__init__(menu=menu, controller=controller)
        options = [
            FunctionItem("Sign up", self.sign_up),
            FunctionItem("Sign in", self.sign_in)
        ]
        for options in options:
            self._menu.append_item(options)