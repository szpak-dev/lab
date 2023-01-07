from dataclasses import dataclass


@dataclass(frozen=True)
class Session:
    id: str
    username: str

from dataclasses import dataclass


@dataclass
class Username:
    value: str


@dataclass
class Password:
    encoded: str


@dataclass
class PlainPassword:
    value: str

    def encode(self) -> Password:
        return Password('password')


@dataclass
class Role:
    name: str


@dataclass
class UserId:
    id: str
