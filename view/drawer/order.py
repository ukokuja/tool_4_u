from view.drawer.base_client_drawer import BaseClientDrawer
from view.drawer.base_drawer import BaseDrawer


class OrderDrawer(BaseClientDrawer):

    def draw(self, instance):
        if self._prompt.prompt_for_bilateral_choice("Would you like to order it?", "Yes", "No") == "Yes":
            self._controller.orders.rental_request(
                client_id=self.client.get('id'),
                item_id=instance.item_id,
                warehouse_id=instance.warehouse_id
            )
        return None, None