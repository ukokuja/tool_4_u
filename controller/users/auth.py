from controller.base_controller import BaseController


class Auth(BaseController):

    def sign_up(self, username, full_name, password):
        # user = self._model.user.create(
        #     first_name=full_name,
        #     email=username,
        #     password=password
        # )
        print("sign up {} {} {}".format(username, password))

    def sign_in(self, username, password):
        print("sign in {} {} {}".format(username, password))
