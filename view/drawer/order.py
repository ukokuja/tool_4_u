from view.drawer.base_drawer import BaseDrawer


class ItemDrawer(BaseDrawer):

    def __init__(self, controller, client):
        super().__init__(controller=controller)
        self.client = client

    def draw(self, instance):
        self._prompt.printf(instance.get_full_description())
        return instance.warehouses, 'warehouses'