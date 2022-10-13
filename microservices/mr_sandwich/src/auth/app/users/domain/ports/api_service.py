from abc import ABC, abstractmethod


class ApiService(ABC):
    @abstractmethod
    def get_user(self, username: str):
        pass
