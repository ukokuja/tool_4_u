from consolemenu import SelectionMenu

from view.console.adaptor import SelectionActionMenu
from view.drawer.base_drawer import BaseDrawer


class ListDrawer(BaseDrawer):

    def __init__(self, controller, title="Please choose an option"):
        super().__init__(controller=controller)
        self.title = title

    def draw(self, instances):
        options = SelectionMenu(title=self.title,
                                exit_option_text="Return to Tool 4 You!",
                                strings=instances)
        options.show()

        return self.handle(options, instances)

    def handle(self, options, instances):
        if options.selected_option < len(instances):
            return instances[options.selected_option], None
        return None, None