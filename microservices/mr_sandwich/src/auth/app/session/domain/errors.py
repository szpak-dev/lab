from app.shared import docstring_message
from app.ddd.domain import DomainError


@docstring_message
class SessionError(DomainError):
    """Session error"""


@docstring_message
class IdentityNotFound(SessionError):
    """Identity was not found within request"""


@docstring_message
class SessionNotFound(SessionError):
    """Session not found"""
