
from view.drawer.list import ListControlDrawer


class UserActiveOrdersDrawer(ListControlDrawer):
    def handle(self, options, instances):
        if options.selected_option < len(instances):
            return instances[options.selected_option], 'order'
        return None, None