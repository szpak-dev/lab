from users.domain.errors import PasswordDoesNotMatch
from users.domain.ports.credentials_checker import CredentialsChecker
from users.domain.value_objects import PlainPassword
from users.domain.ports.user_repository import UserRepository
from shared import emit_events


class UserCredentialsChecker(CredentialsChecker):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def check(self, username: str, plain_password: str) -> None:
        plain_password = PlainPassword(plain_password)
        user = self.user_repository.get_by_username(username)

        try:
            user.check_password(plain_password)
            emit_events(user.release_events())
        except PasswordDoesNotMatch as e:
            emit_events(user.release_events())
            raise e
