from consolemenu import SelectionMenu

from view.console.adaptor import SelectionActionMenu
from view.drawer.base_drawer import BaseDrawer


class ListDrawer(BaseDrawer):

    def draw(self, instances):
        options = SelectionMenu(title="Please choose an option",
                                exit_option_text="Return to Tool 4 You!",
                                strings=instances)
        options.show()

        return self.handle(options, instances)

    def handle(self, options, instances):
        raise NotImplementedError

    if options.selected_option < len(instances):
        return instances[options.selected_option], 'item'
    return None, None