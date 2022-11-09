from cart.domain.value_objects import CustomerId
from cart.infrastructure.in_memory_cart_repository import repository


def provide(customer_id: int):
    return repository.get_active_for_customer(CustomerId(customer_id))
