from abc import ABC, abstractmethod

from users.domain.entities.user import User


class ApiService(ABC):
    @abstractmethod
    def get_user(self, username: str) -> User:
        pass
