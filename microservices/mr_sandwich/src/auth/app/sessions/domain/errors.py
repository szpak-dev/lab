from shared import docstring_message, DomainError


@docstring_message
class SessionError(DomainError):
    """Session error"""


@docstring_message
class IdentityNotFound(SessionError):
    """Identity was not found within flask_request"""


@docstring_message
class SessionNotFound(SessionError):
    """Session not found"""
