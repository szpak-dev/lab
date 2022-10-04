from abc import ABC, abstractmethod

from app.user.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
