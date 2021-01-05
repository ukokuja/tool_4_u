

class Observable(object):
    observers = []

    def add_observer(self, view):
        self.observers.append(view)

    def notify(self, obj):
        for observer in self.observers:
            observer.update(obj)


class Observer(object):

    def update(self, obj):
        raise NotImplementedError
