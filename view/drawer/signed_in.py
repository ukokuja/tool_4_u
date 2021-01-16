from view.drawer.base_drawer import BaseDrawer


class SignedInDrawer(BaseDrawer):

    def draw(self, instance):
        if self._controller.register_auth(instance):
            self._prompt.printf("Welcome %s" % instance)
        elif self._prompt.prompt_for_bilateral_choice("%s, you are already logged in. Would you like to log out?" % instance, "Yes", "No") == "Yes":
            self._controller.remove_auth()
            return None, "logged_out"
        return None, None