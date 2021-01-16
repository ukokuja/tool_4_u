from sqlalchemy import inspect

from view.drawer.base_drawer import BaseDrawer


class BaseClientDrawer(BaseDrawer):

    def __init__(self, controller, client):
        super().__init__(controller=controller)
        self.client = client

    def draw(self, instance):
        inspected_instance = inspect(instance)
        for key in inspected_instance.mapper.column_attrs.keys():
            print("{}: {}".format(key, inspected_instance.dict[key]))
