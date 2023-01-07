from dataclasses import dataclass


@dataclass(frozen=True)
class Session:
    id: str
    username: str


@dataclass(frozen=True)
class SessionId:
    value: str


@dataclass(frozen=True)
class Username:
    value: str


@dataclass(frozen=True)
class Password:
    encoded: str


@dataclass(frozen=True)
class PlainPassword:
    value: str

    def encode(self) -> Password:
        return Password('password')


@dataclass(frozen=True)
class Role:
    name: str


@dataclass(frozen=True)
class UserId:
    id: str
