from dataclasses import dataclass

from app.shared import AggregateRoot
from app.user.domain.value_objects import Role, PlainPassword, Password, Username, UserId
from app.user.domain.errors import PasswordDoesNotMatch


@dataclass
class User(AggregateRoot):
    id: UserId
    username: Username
    role: Role
    password: Password

    def promote(self, role: Role):
        pass

    def demote(self, role: Role):
        pass

    def check_password(self, plain_password: PlainPassword) -> None:
        if self.password.encoded != plain_password.encode().encoded:
            raise PasswordDoesNotMatch


def create_user() -> User:
    return User(
        id=UserId('uid'),
        username=Username('admin_user'),
        password=Password('plain-password'),
        role=Role('SUPER_ADMIN'),
    )