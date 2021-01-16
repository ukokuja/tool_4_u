from view.drawer.base_drawer import BaseDrawer


class ItemDrawer(BaseDrawer):

    def draw(self, instance):
        self._prompt.printf(instance.get_full_description())
        return instance.warehouses, 'warehouses'