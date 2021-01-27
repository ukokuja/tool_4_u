from controller.base_controller import BaseController


class Inventory(BaseController):

    def search(self, title):
        self._model.notify(self._model.item.query(title=title), 'search_results_by_title')

    def search_by_city(self, city_id):
        city = self._model.city.get(id=city_id)
        items = []
        for n in city.neighbourhood:
            for w in n.warehouse:
                for wi in w.items:
                    items.append(wi.item)
        self._model.notify(items, 'search_results_by_city')




