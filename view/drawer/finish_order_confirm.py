from view.drawer.base_drawer import BaseControlDrawer

class FinishOrderConfirmControlDrawer(BaseControlDrawer):

    def draw(self, instance):
        if self._prompt.prompt_for_bilateral_choice("Are you sure?", "Yes", "No") == "Yes":
            self._controller.orders.return_tool(
                order_id=instance.id
            )
        return None, None
