from view.drawer.base_drawer import BaseDrawer


class WarehouseDrawer(BaseDrawer):

    def draw(self, instance):
        self._prompt.printf(instance.get_full_description())
        return instance, 'warehouse'
