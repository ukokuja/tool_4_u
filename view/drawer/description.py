from view.drawer.base_drawer import BaseControlDrawer


class DescriptionControlDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._prompt.printf(instance.get_full_description())
        return None, None
