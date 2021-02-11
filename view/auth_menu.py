from consolemenu.items import FunctionItem
from consolemenu.validators.regex import RegexValidator
from sqlalchemy_utils.types import phone_number

from view.base_menu import BaseMenu
from view.console.adaptor import T4UMenu


class AuthMenu(BaseMenu):

    loggedInUser = None

    def __getattribute__(self, attr):
        method = object.__getattribute__(self, attr)
        if not method:
            raise Exception("Method %s not implemented" % attr)
        if callable(method):
            self._menu.pause()
        return method

    def sign_up(self):
        email = self._prompt_utils.input(prompt='Email', validators=[RegexValidator("^\S+@\S+\.\S+$")])
        while not email or not email.validation_result:
            print("email is not valid, please try again")
            email = self._prompt_utils.input(prompt='Email', validators=[RegexValidator("^\S+@\S+\.\S+$")])

        first_name = self._prompt_utils.input(prompt='First name', validators=[RegexValidator("^[a-zA-Z]{2,}$")])
        while not first_name or not first_name.validation_result:
            print("first name is not valid, please try again")
            first_name = self._prompt_utils.input(prompt='First Name', validators=[RegexValidator("^[a-zA-Z]{2,}$")])

        last_name = self._prompt_utils.input(prompt='Last name', validators=[RegexValidator("^[a-zA-Z]{2,}$")])
        while not last_name or not last_name.validation_result:
            print("last name is not valid, please try again")
            last_name = self._prompt_utils.input(prompt='Last name', validators=[RegexValidator("^[a-zA-Z]{2,}$")])

        phone_number = self._prompt_utils.input(prompt='Phone', validators=[RegexValidator("^[0-9]*$")])
        while not phone_number or not phone_number.validation_result:
            print("phone number is not valid, please try again")
            phone_number = self._prompt_utils.input(prompt='Phone', validators=[RegexValidator("^[0-9]*$")])

        password = self._prompt_utils.prompt_and_confirm_password(message='Password')

        self._controller.auth.sign_up(email=email.input_string,
                                      phone_number=phone_number.input_string,
                                      first_name=first_name.input_string,
                                      last_name=last_name.input_string,
                                      password=password)

    def sign_in(self):
        email = self._prompt_utils.input(prompt='Email', validators=None)
        password = self._prompt_utils.input_password(message='Password')
        self.loggedInUser = self._controller.auth.sign_in(email=email.input_string,
                                      password=password)

    def __init__(self, menu, controller):
        super().__init__(menu=menu, controller=controller)
        options = [
            FunctionItem("Sign up", self.sign_up),
            FunctionItem("Sign in", self.sign_in)
        ]
        for options in options:
            self._menu.append_item(options, T4UMenu.USER_LOGGED_OUT)
