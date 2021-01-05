class ViewSet(object):

    def get(self, id):
        return self._session.query(self._entity).get(id)

    def list(self):
        self._session.query(self._entity).all()

    def create(self, **kwargs):
        self._session.insert(self._entity(**kwargs))

    def update(self, **kwargs):
        self._session.update(self._entity(**kwargs))

    def delete(self, id):
        self._session.delete(self._entity, id=id)


class ControllerManager(object):
    def __init__(self, model):
        self.__model = model
