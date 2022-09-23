from abc import ABC, abstractmethod

from app.user.adapters.db.in_memory_user_repository import InMemoryUserRepository

user_repository = InMemoryUserRepository()


class Authenticator(ABC):
    @abstractmethod
    def check_credentials(self, credentials: Credentials):
        pass
