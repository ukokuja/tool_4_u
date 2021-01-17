
class ViewSetMock(object):

    def create(self, **kwargs):
        return kwargs

    def query(self, **kwargs):
        return kwargs


class ModelMock:
    def __init__(self):
        self.client = ViewSetMock()
        self.item = ViewSetMock()
        self.response = None

    #workaround for observer pattern
    def notify(self, object, label):
        self.response = (object, label)

    #workaround for observer pattern
    def get_response(self):
        return self.response
