from view.drawer.base_drawer import BaseDrawer


class ClientDrawer(BaseDrawer):

    def draw(self, instance):
        if self._prompt.prompt_for_bilateral_choice("%s created, would you like to sign in?" % instance.first_name, "Yes", "No") == "Yes":
            return instance, 'sign_in'
        return None, None