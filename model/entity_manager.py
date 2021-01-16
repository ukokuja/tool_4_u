from controller import ViewSet


class EntityManager(ViewSet):

    def __init__(self, session, entity):
        self._session = session
        self._entity = entity