from controller.base_controller import BaseController


class Inventory(BaseController):

    def search(self, query):
        self._model.notify(self._model.item.query(title=query))
