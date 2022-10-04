from app.user.domain.ports.credentials_checker import CredentialsChecker
from app.user.domain.value_objects import PlainPassword
from app.user.adapters import user_repository
from app.user.domain.errors import UserNotFound


class UserCredentialsChecker(CredentialsChecker):
    def check(self, username: str, plain_password: str) -> None:
        user = user_repository().get_by_username(username)
        if not user:
            raise UserNotFound

        password = PlainPassword(plain_password)
        user.check_password(password)
