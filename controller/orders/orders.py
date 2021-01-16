from controller.base_controller import BaseController

class Orders(BaseController):
    def rental_request(self, client_id, item_id, warehouse_id):
        self._model.notify(self._model.order.create(
            client_id=client_id,
            item_id=item_id,
            warehouse_id=warehouse_id
        ))

    def return_tool(self):
        pass