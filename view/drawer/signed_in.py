from view.drawer.base_drawer import BaseDrawer


class SignInDrawer(BaseDrawer):

    def draw(self, instance):
        self._prompt.printf("Welcome %s" % instance.full_name)
        return None, None