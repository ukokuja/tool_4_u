from view.drawer.base_drawer import BaseControlDrawer


class CityDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._controller.inventory.search_by_city(instance.id)
        return None, None