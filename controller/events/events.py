from controller.base_controller import BaseController
from model import Order, Item


class Events(BaseController):

    def send_event(self, **kwargs):
        self._model.event.create(**kwargs)

    def unreturned_items(self):
        orders = self._model.order.get_query() \
            .filter(Order.end_date == None)
        self._model.notify(orders.all(), 'show_users_active_orders')

    def most_ordered_items(self):
        orders = self._model.order.group_by(Order.item_id, Order.item_id)
        items = self._model.item.advanced_query(Item.id.in_([x[1] for x in orders]))
        for order in orders:
            for item in items:
                if order[1] == item.id:
                    item.count = order[0]
        self._model.notify(items, 'most_ordered_items')

    def track_user(self, user_id=None):
        if user_id:
            self._model.notify(self._model.event.query(client_id=user_id), 'track_user')
        else:
            return self._model.user.list()

