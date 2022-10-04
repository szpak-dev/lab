from dataclasses import dataclass
from random import randrange
from typing import TypeVar


@dataclass
class Credentials:
    username: str
    password: str


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
        chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        steps = range(0, length)

        num = []
        for step in steps:
            character_index = randrange(0, len(chars) - 1)
            num.append(chars[character_index])

        number = ''.join(num)
        return SessionId(number)
