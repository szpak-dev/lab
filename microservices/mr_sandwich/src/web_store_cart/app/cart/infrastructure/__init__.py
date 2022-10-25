from cart.domain.repository import CartRepository
from cart.infrastructure.in_memory_cart_repository import InMemoryCartRepository

cart_repository: CartRepository = InMemoryCartRepository()
