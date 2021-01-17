
from view.drawer.list import ListDrawer


class ActiveOrdersDrawer(ListDrawer):
    def handle(self, options, instances):
        if options.selected_option < len(instances):
            return instances[options.selected_option], 'finish_order'
        return None, None