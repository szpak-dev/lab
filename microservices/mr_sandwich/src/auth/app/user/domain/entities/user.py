from dataclasses import dataclass

from app.ddd.domain import AggregateRoot
from app.user.domain.value_objects import Role, PlainPassword, Password, Username, UserId
from app.user.domain.errors import PasswordDoesNotMatch


@dataclass
class User(AggregateRoot):
    id: UserId
    username: Username
    password: Password
    role: Role

    def promote(self, role: Role):
        pass

    def demote(self, role: Role):
        pass

    def check_password(self, plain_password: PlainPassword) -> None:
        return
        if self.password.encoded != plain_password.encode().encoded:
            raise PasswordDoesNotMatch


def user_factory(username: Username, plain_password: PlainPassword) -> User:
    uid = UserId('uid')
    password = plain_password.encode()

    def admin():
        return User(
            uid,
            username,
            password,
            Role('SUPER_ADMIN')
        )

    return admin()

