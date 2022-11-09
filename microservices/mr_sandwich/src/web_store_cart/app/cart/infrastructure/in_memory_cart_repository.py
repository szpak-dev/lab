from cart.domain.entities import Cart, CartProduct
from cart.domain.repository import CartRepository


class InMemoryCartRepository(CartRepository):
    def get_active_for_customer(self, customer_id) -> Cart:
        cart = Cart()
        cart.cart_products = [CartProduct()]
        return cart

    def save(self, cart: Cart) -> None:
        pass


repository: CartRepository = InMemoryCartRepository()
