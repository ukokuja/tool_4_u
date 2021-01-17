

class Observable(object):
    observers = []

    def add_observer(self, view):
        self.observers.append(view)

    def notify(self, obj, label):
        for observer in self.observers:
            observer.update(obj, label)


class Observer(object):

    def update(self, obj, label):
        raise NotImplementedError
