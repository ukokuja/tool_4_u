from consolemenu import SelectionMenu

from view.console.adaptor import SelectionActionMenu
from view.drawer.base_drawer import BaseDrawer


class ItemListDrawer(BaseDrawer):


    def handle(self, options, instances):
        if options.selected_option < len(instances):
            return instances[options.selected_option], 'item'
        return None, None