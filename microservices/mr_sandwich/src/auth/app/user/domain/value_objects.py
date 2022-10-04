from dataclasses import dataclass


@dataclass
class Password:
    encoded: str


@dataclass
class PlainPassword:
    plain: str

    def encode(self) -> Password:
        return Password('hashed-encoded')


@dataclass
class Role:
    role: str


@dataclass
class UserId:
    id: str


@dataclass
class Username:
    username: str
