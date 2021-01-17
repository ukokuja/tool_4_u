from controller.base_controller import BaseController


class Inventory(BaseController):

    def search(self, title):
        self._model.notify(self._model.item.query(title=title), 'search_results_by_title')

    def search_by_city(self, city):
        self._model.notify(self._model.city.query(name=city), 'search_results_by_city')

