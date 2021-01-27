from view.drawer.base_client_drawer import BaseClientControlDrawer
from view.drawer.base_drawer import BaseControlDrawer


class ConfirmOrderDrawer(BaseClientControlDrawer):

    def draw(self, instance):
        if self._prompt.prompt_for_bilateral_choice("Would you like to order it?", "Yes", "No") == "Yes":
            self._controller.orders.rental_request(
                client_id=self._controller.get_client_prop('id'),
                item_id=instance.item_id,
                warehouse_id=instance.warehouse_id
            )
        return None, None