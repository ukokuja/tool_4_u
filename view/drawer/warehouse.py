from view.drawer.base_drawer import BaseControlDrawer


class WarehouseControlDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._prompt.printf(instance.get_full_description())
        return instance, 'warehouse'
