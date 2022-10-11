from app.shared import docstring_message
from app.ddd.domain import DomainError


@docstring_message
class UserError(DomainError):
    """User error"""


@docstring_message
class UserAlreadyExists(UserError):
    """User already exists"""


@docstring_message
class UserNotFound(UserError):
    """User not found"""


@docstring_message
class PasswordDoesNotMatch(UserError):
    """Password is invalid"""
