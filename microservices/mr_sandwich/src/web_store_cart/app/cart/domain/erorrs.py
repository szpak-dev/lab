from shared.shared import docstring_message, DomainError


@docstring_message
class CartError(DomainError):
    """Cart error"""


@docstring_message
class CartNotFound(CartError):
    """Cart not found"""


@docstring_message
class ProductNotInCart(CartError):
    """Given Product is not in this Cart"""


@docstring_message
class CartIsBeingProcessed(CartError):
    """Cart operations in progress, please retry"""