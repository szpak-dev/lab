from app.user.domain.ports.user_repository import UserRepository
from app.user.adapters.user_authenticator import UserAuthenticator


def user_repository() -> UserRepository:
    return UserRepository()


def authenticator() -> UserAuthenticator:
    return UserAuthenticator()
