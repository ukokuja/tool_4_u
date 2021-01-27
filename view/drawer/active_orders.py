
from view.drawer.list import ListControlDrawer


class ActiveOrdersDrawer(ListControlDrawer):
    def handle(self, options, instances):
        if options.selected_option < len(instances):
            return instances[options.selected_option], 'finish_order'
        return None, None