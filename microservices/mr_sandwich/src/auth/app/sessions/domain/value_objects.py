from dataclasses import dataclass
from typing import TypeVar

from shared import generate_number_base64
from users.domain.value_objects import Username, Password


@dataclass
class Credentials:
    username: str
    password: str

    @classmethod
    def new(cls, username: str, password: str):
        return Credentials(
            username=username,
            password=password,
        )

    def username(self) -> Username:
        return Username(self.username)

    def password(self) -> Password:
        return Password(self.password)


@dataclass
class Jwt:
    jwt: str


@dataclass
class Identity:
    def __init__(self, session_id=None, jwt=None):
        if session_id is None and jwt is None:
            raise RuntimeError('No Identity found')

        self._session_id = session_id
        self._jwt = jwt

    def requested_from_internet(self):
        return type(self._session_id) is SessionId

    def requested_from_subnet(self):
        return type(self._jwt) is Jwt

    def value(self) -> str:
        if self._session_id is not None:
            return self._session_id.id

        return self._jwt.jwt


SID = TypeVar('SID', bound='SessionId')


@dataclass(frozen=True)
class SessionId:
    id: str

    def raw(self):
        return self.id

    @staticmethod
    def new() -> SID:
        number = generate_number_base64(40)
        return SessionId(id=number)
