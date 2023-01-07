from abc import abstractmethod

from shared.ddd import BaseRepository
from domain.entities import User
from domain.value_objects import Username, PlainPassword


class UserRepository(BaseRepository):
    @abstractmethod
    def get_by_username(self, username: Username) -> User:
        pass

    @abstractmethod
    def add_new(self, username: Username, plain_password: PlainPassword) -> None:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass
