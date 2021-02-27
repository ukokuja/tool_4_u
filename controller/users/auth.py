from controller.base_controller import BaseController
from passlib.hash import bcrypt


class Auth(BaseController):

    def sign_up(self, email, phone_number, first_name, last_name, password):
        self._model.notify(self._model.client.create(
            plan_id=1,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            email=email,
            role_id=1,
            password=bcrypt.hash(password),
        ), 'sign_up')

    def sign_in(self, email, password):
        client = self._model.client.get(email=email)
        if client and bcrypt.verify(password, client.password):
            self._model.notify(client, 'sign_in')
        else:
            self._model.notify(None, 'wrong_password')


    def sign_out(self):
        self._model.notify(None, 'sign_out')