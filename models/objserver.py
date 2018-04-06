class Observer():

    def update(self, **kwargs):
        pass


class Observable():

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
        else:
            print('Error: Failed to add.')

    def remove_observer(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            print('Error: Failed to remove.')

    def notify_all(self, **kwargs):
        for observer in self.observers:
            observer.update(self, **kwargs)