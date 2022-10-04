from app.user.domain.ports.user_repository import UserRepository
from app.user.adapters.user_credentials_checker import UserCredentialsChecker
from app.user.adapters.in_memory_user_repository import InMemoryUserRepository


def user_repository() -> UserRepository:
    return InMemoryUserRepository()


def authenticator() -> UserCredentialsChecker:
    return UserCredentialsChecker()
