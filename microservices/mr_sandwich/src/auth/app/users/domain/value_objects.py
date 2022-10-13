from dataclasses import dataclass


@dataclass
class Password:
    encoded: str


@dataclass
class PlainPassword:
    value: str

    def encode(self) -> Password:
        return Password('hashed-encoded')


@dataclass
class Role:
    value: str


@dataclass
class UserId:
    id: str


@dataclass
class Username:
    value: str
