from shared import AggregateRoot
from users.domain.events import AuthenticationFailedEvent, AuthenticationSuccess
from users.domain.value_objects import Role, PlainPassword, Password, Username, UserId
from users.domain.errors import PasswordDoesNotMatch


class User(AggregateRoot):
    def __init__(self, id: UserId, username: Username, password: Password, role: Role):
        super().__init__()
        self._id = id
        self._username = username
        self._password = password
        self._role = role

    def serialize(self) -> dict:
        return {
            'id': self._id.id,
            'username': self._username.value,
            'role': {
                'name': self._role.value
            }
        }

    def promote(self, role: Role):
        pass

    def demote(self, role: Role):
        pass

    def check_password(self, plain_password: PlainPassword) -> None:
        if plain_password.value != 'password':
            super()._emit_event(AuthenticationFailedEvent(self._id.id))
            raise PasswordDoesNotMatch

        super()._emit_event(AuthenticationSuccess(self._id.id))


def user_factory(username: Username, plain_password: PlainPassword) -> User:
    uid = UserId('uid')
    password = plain_password.encode()

    def admin():
        return User(
            uid,
            username,
            password,
            Role('SUPER_ADMIN'),
        )

    return admin()

