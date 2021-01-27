
class ViewSet(object):

    def get(self, id=None, **kwargs):
        if id:
            return self._session.query(self._entity).get(id)
        return self._session.query(self._entity).filter_by(**kwargs).first()

    def query(self, **kwargs):
        return self._session.query(self._entity).filter_by(**kwargs).all()

    def get_query(self):
        return self._session.query(self._entity)

    def list(self):
        return self._session.query(self._entity).all()

    def create(self, **kwargs):
        entity = self._entity(**kwargs)
        self._session.add(entity)
        self._session.commit()
        self._session.refresh(entity)
        return entity

    def update(self, values, **filter):
        entity = self._session.query(self._entity).filter_by(**filter)
        entity.update(values=values)
        self._session.commit()

    def delete(self, id):
        return self._session.delete(self._entity, id=id)
