from app.shared import docstring_message


class SessionError(Exception):
    pass


@docstring_message
class IdentityNotFound(SessionError):
    """Identity was not found within request"""


@docstring_message
class SessionNotFound(SessionError):
    """Session not found"""
