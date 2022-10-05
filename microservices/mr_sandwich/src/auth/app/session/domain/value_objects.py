from dataclasses import dataclass
from typing import TypeVar

from app.shared import generate_number_base64
from app.user.domain.value_objects import Username, Password


@dataclass
class Credentials:
    username: str
    password: str

    def username(self):
        return Username(self.username)

    def password(self):
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


@dataclass
class Session:
    id: str


T = TypeVar('T', bound='SessionId')


@dataclass
class SessionId:
    id: str

    @staticmethod
    def generate(length: int = 20) -> T:
        number = generate_number_base64(length)
        return SessionId(number)
