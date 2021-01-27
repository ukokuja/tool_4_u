from consolemenu import PromptUtils, Screen
from sqlalchemy import inspect

class BaseDrawer():

    def __init__(self):
        self._prompt = PromptUtils(Screen())


    def draw(self, instance):
        inspected_instance = inspect(instance)
        for key in inspected_instance.mapper.column_attrs.keys():
            print("{}: {}".format(key, inspected_instance.dict[key]))

class BaseControlDrawer(BaseDrawer):

    def __init__(self, controller):
        super().__init__()
        self._controller = controller
