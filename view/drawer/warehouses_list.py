from view.drawer.list import ListDrawer


class WarehousesListDrawer(ListDrawer):

    def handle(self, options, instances):
        if options.selected_option < len(instances):
            return instances[options.selected_option], 'confirm_order'
        return None, None
