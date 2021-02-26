from view.drawer.base_drawer import BaseControlDrawer

class AddCityDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'cities_to_add')

class AddNeighbourhoodDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'neighbourhood_to_add')

class AddWarehouseDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'warehouse_to_add')

class AddItemDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'item_to_add')

class EditCityDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'cities_to_edit')

class EditNeighbourhoodDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'neighbourhood_to_edit')

class EditWarehouseDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'warehouse_to_edit')

class EditItemDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'item_to_edit')

class RemoveCityDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'cities_to_remove')

class RemoveNeighbourhoodDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'neighbourhood_to_remove')

class RemoveWarehouseDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'warehouse_to_remove')

class RemoveItemDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._model.notify(self._model.city.list(), 'item_to_remove')
