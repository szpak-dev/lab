from cart.domain.entities import Cart
from cart.domain.repository import CartRepository


class InMemoryCartRepository(CartRepository):
    def get_active_for_customer(self, customer_id) -> Cart:
        pass

    def save(self, cart: Cart) -> None:
        pass


repository: CartRepository = InMemoryCartRepository()
