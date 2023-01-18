from cart.domain.entities import Cart
from cart.domain.value_objects import CustomerId
from cart.infrastructure import cart_repository


async def provide(customer_id: int) -> Cart:
    return await cart_repository.get_active_for_customer(CustomerId(customer_id))
