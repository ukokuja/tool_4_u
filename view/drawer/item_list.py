from view.drawer.base_drawer import BaseControlDrawer


class ItemListControlDrawer(BaseControlDrawer):


    def handle(self, options, instances):
        if options.selected_option < len(instances):
            return instances[options.selected_option], 'item'
        return None, None