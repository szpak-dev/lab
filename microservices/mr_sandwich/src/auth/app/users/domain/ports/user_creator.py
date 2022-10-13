from abc import ABC, abstractmethod


class UserCreator(ABC):
    @abstractmethod
    def create(self, username: str, password: str):
        pass
