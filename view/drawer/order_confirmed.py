from view.drawer.base_drawer import BaseDrawer

class OrderConfirmedDrawer(BaseDrawer):

    def draw(self, instance):
        self._prompt.enter_to_continue("Order confirmed")
        return None, None
