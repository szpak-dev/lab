from datetime import datetime


class DomainEvent:
    """Represents default DomainEvent, all other Events inherits from it"""
    def __init__(self, name='Event', data=None):
        if data is None:
            data = {}

        self._name = name
        self._fired_at = datetime.now()
        self._data = data

    def get_data(self, key):
        return self._data[key]
