from consolemenu import PromptUtils, Screen
from sqlalchemy import inspect


class BaseDrawer():

    def __init__(self, controller):
        self._prompt = PromptUtils(Screen())
        self._controller = controller

    def draw(self, instance):
        inspected_instance = inspect(instance)
        for key in inspected_instance.mapper.column_attrs.keys():
            print("{}: {}".format(key, inspected_instance.dict[key]))
