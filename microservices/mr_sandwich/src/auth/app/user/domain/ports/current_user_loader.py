from abc import ABC, abstractmethod


class CurrentUserLoader(ABC):
    @abstractmethod
    def load(self):
        raise NotImplementedError
