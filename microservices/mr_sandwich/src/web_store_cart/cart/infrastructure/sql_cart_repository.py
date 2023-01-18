from sqlalchemy.exc import NoResultFound
from sqlalchemy.future import select

from cart.domain.entities import Cart, CartProduct
from cart.domain.erorrs import CartNotFound
from cart.domain.repository import CartRepository
from cart.domain.value_objects import CustomerId
from shared.async_db import async_session


class SqlCartRepository(CartRepository):
    async def get_active_for_customer(self, customer_id: CustomerId) -> Cart:
        customer_id = customer_id.id
        async with async_session() as session:
            try:
                result = await session.execute(
                    select(Cart)
                    .filter(
                        Cart.customer_id == customer_id,
                        Cart.status == 'ACTIVE',
                    )
                    .join(CartProduct, isouter=True)
                )

                return result.unique().scalars().one()
            except NoResultFound:
                raise CartNotFound

    async def save(self, cart: Cart) -> None:
        async with async_session() as session:
            session.add(cart)
            await session.commit()
