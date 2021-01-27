import datetime

from controller.base_controller import BaseController
from model import Order


class Orders(BaseController):
    def rental_request(self, client_id, item_id, warehouse_id):
        self._model.notify(self._model.order.create(
            client_id=client_id,
            item_id=item_id,
            warehouse_id=warehouse_id
        ), 'order_created')

    def return_tool(self, order_id):
        self._model.order.update(values={
            "end_date": datetime.datetime.utcnow()
        }, id=order_id)

    def show_active_orders(self, client_id):
        orders = self._model.order.get_query() \
            .filter(Order.end_date == None, Order.client_id == client_id)
        self._model.notify(orders.all(), 'show_active_orders')

    def show_expired_orders(self, client_id):
        orders = self._model.order.get_query() \
            .filter(Order.end_date.isnot(None), Order.client_id == client_id)
        self._model.notify(orders.all(), 'show_expired_orders')

    def show_orders(self, client_id):
        self._model.notify(self._model.order.query(
            client_id=client_id
        ), 'show_orders')
