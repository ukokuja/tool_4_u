
class ViewSetMock(object):

    def create(self, **kwargs):
        return kwargs

    def query(self, **kwargs):
        return kwargs

    def get_query(self, query):
        return query

    def advanced_query(self, query):
        return query

    def update(self, values, **filter):
        return values


class ModelMock:
    def __init__(self):
        self.client = ViewSetMock()
        self.item = ViewSetMock()
        self.user = ViewSetMock()
        self.inventory = ViewSetMock()
        self.order = ViewSetMock()
        self.response = None

    #workaround for observer pattern
    def notify(self, object, label):
        self.response = (object, label)

    #workaround for observer pattern
    def get_response(self):
        return self.response
