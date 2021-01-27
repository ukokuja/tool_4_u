from view.drawer.base_drawer import BaseControlDrawer

class OrderConfirmedControlDrawer(BaseControlDrawer):

    def draw(self, instance):
        self._prompt.enter_to_continue("Order confirmed [Enter to continue]")
        return None, None
