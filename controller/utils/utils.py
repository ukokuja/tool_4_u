from controller.base_controller import BaseController


class Utils(BaseController):

    def get_cities(self):
        self._model.notify(self._model.city.list(), 'cities')

