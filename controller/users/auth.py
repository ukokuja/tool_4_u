from controller.base_controller import BaseController


class Auth(BaseController):

    def sign_up(self, email, phone_number, first_name, last_name, password):

        self._model.notify(self._model.client.create(
            plan_id=1,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        ), 'sign_up')

    def sign_in(self, email, password):
        self._model.notify(self._model.client.get(
            email=email,
            password=password
        ), 'sign_in')
