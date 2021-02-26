from view.drawer.base_drawer import BaseDrawer


class MessageDrawer(BaseDrawer):

    def __init__(self, message):
        super().__init__()
        self.message = message

    def draw(self, instance=None):
        self._prompt.enter_to_continue(self.message)
        return None, None
