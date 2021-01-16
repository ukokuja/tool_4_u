from controller.base_controller import BaseController


class Auth(BaseController):

    def sign_up(self, username, full_name, password):
        user = self._model.user.create(
            first_name=full_name,
            email=username,
            password=password
        )
        self._model.notify(self._model.client.create(
            id = user.id,
            plan_id=1,
            phone_number=full_name,
        ))

    def sign_in(self, username, password):
        print("sign in {} {} {}".format(username, password))
