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
        }, id=user_id), 'update user phone number')

    def edit_user_role(self, user_id=None, role_id=None):
        if user_id:
            if role_id:
                self._model.notify(self._model.user.update(
                    values={
                        "role_id": role_id
                    }, id=user_id
                ), 'user_updated')
            else:
                return self._model.role.list()
        else:
            return self._model.user.list()
