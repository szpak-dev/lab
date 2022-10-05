from app.user.domain.ports.credentials_checker import CredentialsChecker
from app.user.domain.value_objects import PlainPassword
from app.user.domain.ports.user_repository import UserRepository


class UserCredentialsChecker(CredentialsChecker):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def check(self, username: str, plain_password: str) -> None:
        plain_password = PlainPassword(plain_password)

        user = self.user_repository.get_by_username(username)
        user.check_password(plain_password)
