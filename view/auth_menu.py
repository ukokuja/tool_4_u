from consolemenu.items import FunctionItem

from view.base_menu import BaseMenu


class AuthMenu(BaseMenu):
    def __getattribute__(self, attr):
        method = object.__getattribute__(self, attr)
        if not method:
            raise Exception("Method %s not implemented" % attr)
        if callable(method):
            self._menu.pause()
        return method

    def sign_up(self):
        email = self._prompt_utils.input(prompt='Email', validators=None)
        first_name = self._prompt_utils.input(prompt='First name', validators=None)
        last_name = self._prompt_utils.input(prompt='Last name', validators=None)
        phone_number = self._prompt_utils.input(prompt='Phone', validators=None)
        password = self._prompt_utils.prompt_and_confirm_password(message='Password')

        self._controller.auth.sign_up(email=email.input_string,
                                      phone_number=phone_number.input_string,
                                      first_name=first_name.input_string,
                                      last_name=last_name.input_string,
                                      password=password)

    def sign_in(self):
        email = self._prompt_utils.input(prompt='Email', validators=None)
        password = self._prompt_utils.input_password(message='Password')
        self._controller.auth.sign_in(email=email.input_string,
                                      password=password)

    def __init__(self, menu, controller):
        super().__init__(menu=menu, controller=controller)
        options = [
            FunctionItem("Sign up", self.sign_up),
            FunctionItem("Sign in", self.sign_in)
        ]
        for options in options:
            self._menu.append_item(options)
