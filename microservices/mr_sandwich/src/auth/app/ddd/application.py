from abc import ABC, abstractmethod


class ApplicationCommand:
    pass


class ApplicationQuery(ABC):
    @abstractmethod
    def result(self):
        pass
