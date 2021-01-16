from controller.base_controller import BaseController


class Inventory(BaseController):

    def search(self, title):
        self._model.notify(self._model.item.query(title=title))

    def search_by_city(self, city):
        self._model.notify(self._model.city.query(name=city))

