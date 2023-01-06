from cart.domain.entities import Cart
from cart.domain.value_objects import CustomerId
from cart.infrastructure import cart_repository


def provide(customer_id: int) -> Cart:
    return cart_repository.get_active_for_customer(CustomerId(customer_id))
