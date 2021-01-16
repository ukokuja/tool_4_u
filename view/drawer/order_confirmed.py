from view.drawer.base_drawer import BaseDrawer


class OrderDrawer(BaseDrawer):

    def __init__(self, controller, client):
        super().__init__(controller=controller)
        self.client = client

    def draw(self, instance):
        if self._prompt.prompt_for_bilateral_choice("Would you like to order it?", "Yes", "No") == "Yes":
            return instance, 'order_confirmed'
        return None, None