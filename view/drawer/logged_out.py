from view.drawer.base_drawer import BaseControlDrawer


class LoggedOutControlDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._prompt.printf("You've logged out")
        return None, None