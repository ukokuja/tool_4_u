from view.drawer.base_drawer import BaseDrawer


class ClientDrawer(BaseDrawer):

    def draw(self, instance):
        if self._prompt.prompt_for_bilateral_choice("%s created, would you like to sign in?" % instance, "Yes", "No") == "Yes":
            return instance, 'signed_in'
        return None, None