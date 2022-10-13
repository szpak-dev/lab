from dataclasses import dataclass
from enum import Enum

from mediator import MediatorEvent


class BusEvent(Enum):
    AUTHENTICATION_STARTED: str = 'authentication_started'
    CREDENTIALS_CONFIRMED: str = 'credentials_confirmed'
    AUTHENTICATION_SUCCESSFUL: str = 'authentication_successful'


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
