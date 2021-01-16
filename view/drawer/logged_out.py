from view.drawer.base_drawer import BaseDrawer


class LoggedOutDrawer(BaseDrawer):

    def draw(self, instance):
        self._prompt.printf("You've logged out")
        return None, None