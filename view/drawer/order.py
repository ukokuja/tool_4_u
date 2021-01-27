from view.drawer.base_drawer import BaseControlDrawer


class OrderDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._prompt.printf(instance.get_full_description())
        self._prompt.enter_to_continue("\n[Enter to continue]")
        return None, None