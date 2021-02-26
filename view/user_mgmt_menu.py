from consolemenu import SelectionMenu
from consolemenu.items import SubmenuItem
from consolemenu.validators.regex import RegexValidator

from view.base_menu import BaseMenu
from view.console.adaptor import SelectionActionMenu, T4UMenu


class UserMgmtMenu(BaseMenu):
    def __init__(self, menu, controller):
        super().__init__(menu=menu, controller=controller)
        level_1 = SelectionActionMenu(actions=[
            {"title": "Edit First Name", "action": self.edit_first_name},
            {"title": "Edit last Name", "action": self.edit_last_name},
            {"title": "Edit Email", "action": self.edit_email},
            {"title": "Edit Phone Number", "action": self.edit_phone_number},
        ])
        level_2 = SubmenuItem("Edit User Details", level_1, menu)
        self._menu.append_item(level_2, T4UMenu.USER_LOGGED_IN)

        level_1_manager = SelectionActionMenu(actions=[
            {"title": "Edit user role", "action": self.edit_user_role},
        ])
        level_2_manager = SubmenuItem("User management", level_1_manager, menu)
        self._menu.append_item(level_2_manager, T4UMenu.USER_IS_MANAGER)

    def edit_first_name(self):
        client = self._controller.get_client()
        print(f"Current Name: {client.first_name}")

        first_name = self._prompt_utils.input(prompt='New First name', validators=[RegexValidator("^[a-zA-Z]{2,}$")])
        while not first_name or not first_name.validation_result:
            print("first name is not valid, please try again")
            first_name = self._prompt_utils.input(prompt='New First Name',
                                                  validators=[RegexValidator("^[a-zA-Z]{2,}$")])

        self._controller.user_mgmt.change_first_name(client.id, first_name.input_string)

    def edit_last_name(self):
        client = self._controller.get_client()
        print(f"Current Last Name: {client.last_name}")

        last_name = self._prompt_utils.input(prompt='New Last name', validators=[RegexValidator("^[a-zA-Z]{2,}$")])
        while not last_name or not last_name.validation_result:
            print("last name is not valid, please try again")
            last_name = self._prompt_utils.input(prompt='New Last Name', validators=[RegexValidator("^[a-zA-Z]{2,}$")])

        self._controller.user_mgmt.change_last_name(client.id, last_name.input_string)

    def edit_email(self):
        client = self._controller.get_client()
        print(f"Current Email: {client.email}")

        email = self._prompt_utils.input(prompt='New Email', validators=[RegexValidator("^\S+@\S+\.\S+$")])
        while not email or not email.validation_result:
            print("email is not valid, please try again")
            email = self._prompt_utils.input(prompt='New Email', validators=[RegexValidator("^\S+@\S+\.\S+$")])

        self._controller.user_mgmt.change_email(client.id, email.input_string)

    def edit_phone_number(self):
        client = self._controller.get_client()
        print(f"Current Phone Number: {client.phone_number}")

        phone = self._prompt_utils.input(prompt='New Phone Number', validators=[RegexValidator("^[0-9]*$")])
        while not phone or not phone.validation_result:
            print("phone number is not valid, please try again")
            phone = self._prompt_utils.input(prompt='New Phone Number', validators=[RegexValidator("^[0-9]*$")])

        self._controller.user_mgmt.change_phone_number(client.id, phone.input_string)

    def edit_user_role(self):
        users = self._controller.user_mgmt.edit_user_role()
        options = SelectionMenu(title="Choose a user",
                                exit_option_text="Return to Tool 4 You!",
                                strings=users)
        options.show()
        user_id = options.selected_item.text.id
        roles = self._controller.user_mgmt.edit_user_role(user_id=user_id)
        options = SelectionMenu(title="Choose a role",
                                exit_option_text="Return to Tool 4 You!",
                                strings=roles)
        options.show()
        self._controller.user_mgmt.edit_user_role(user_id=user_id, role_id=options.selected_item.text.id)