from controller.base_controller import BaseController


class Auth(BaseController):

    def sign_up(self, username, full_name, password):
        print("sign up {} {} {}".format(username, full_name, password))

    def sign_in(self, username, password):
        print("sign in {} {} {}".format(username, password))
