from dataclasses import dataclass

from app.shared import MediatorEvent


@dataclass
class AuthenticationStarted(MediatorEvent):
    username: str
    password: str


@dataclass
class AuthenticationSuccessful(MediatorEvent):
    pass


@dataclass
class CredentialsConfirmed(MediatorEvent):
    username: str
