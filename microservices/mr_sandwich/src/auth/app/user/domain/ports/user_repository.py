from abc import ABC, abstractmethod

from app.user.domain.models.user import User
from app.user.domain.models.username import Username


class UserRepository(ABC):
    @abstractmethod
    def get_by_username(self, username: Username) -> User:
        pass

    @abstractmethod
    def compare_password(self, user: User, plain_password: str) -> bool:
        pass
