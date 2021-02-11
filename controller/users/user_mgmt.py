from controller.base_controller import BaseController


class UserMgmt(BaseController):

    def change_first_name(self, user_id, name):
        self._model.notify(self._model.user.update(values={
            "first_name": name
        }, id=user_id), 'update user first name')

    def change_last_name(self, user_id, name):
        self._model.notify(self._model.user.update(values={
            "last_name": name
        }, id=user_id), 'update user last name')

    def change_email(self, user_id, email):
        self._model.notify(self._model.user.update(values={
            "email": email
        }, id=user_id), 'update user email')


    def change_phone_number(self, user_id, phone_number):
        self._model.notify(self._model.client.update(values={
            "phone_number": phone_number
        }, id=user_id), 'update client phone number')