from abc import abstractmethod

from app.user.domain.entities.user import User
from app.shared import BaseRepository


class UserRepository(BaseRepository):
    @abstractmethod
    def get_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
