from cart.domain.entities import Cart, CartProduct
from cart.domain.erorrs import CartNotFound
from cart.domain.repository import CartRepository
from cart.domain.value_objects import CustomerId
from shared.db import db_session


class SqlCartRepository(CartRepository):
    def get_active_for_customer(self, customer_id: CustomerId) -> Cart:
        cart = db_session.query(Cart).filter(
            Cart.customer_id == customer_id.id,
            Cart.status == 'ACTIVE'
        ).join(CartProduct, isouter=True).first()

        if not cart:
            raise CartNotFound

        return cart

    def save(self, cart: Cart) -> None:
        with db_session as session:
            session.add(cart)
            session.commit()
