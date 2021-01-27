from sqlalchemy import inspect

from view.drawer.base_drawer import BaseControlDrawer


class BaseClientControlDrawer(BaseControlDrawer):

    def __init__(self, controller: object) -> object:
        super().__init__(controller=controller)
        self.client = controller.get_client()

    def draw(self, instance):
        inspected_instance = inspect(instance)
        for key in inspected_instance.mapper.column_attrs.keys():
            print("{}: {}".format(key, inspected_instance.dict[key]))
