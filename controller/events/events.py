from controller.base_controller import BaseController


class Events(BaseController):

    def send_event(self, **kwargs):
        self._model.event.create(**kwargs)
