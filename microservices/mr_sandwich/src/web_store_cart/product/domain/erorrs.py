from shared.ddd import DomainError
from shared.shared import docstring_message


@docstring_message
class ProductError(DomainError):
    """Product error"""


@docstring_message
class ProductNotFound(ProductError):
    """Product not found"""

