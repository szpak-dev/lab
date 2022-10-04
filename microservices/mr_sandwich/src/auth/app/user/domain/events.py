from dataclasses import dataclass

from app.shared import DomainEvent


@dataclass
class UserCreated(DomainEvent):
    super('auth.user.created')
    user_id: str


@dataclass
class UserPromoted(DomainEvent):
    super('auth.user.promoted')
    user_id: str


@dataclass
class UserDemoted(DomainEvent):
    super('auth.user.demoted')
    user_id: str
