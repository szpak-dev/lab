from cart.domain.repository import CartRepository
from cart.infrastructure.sql_cart_repository import SqlCartRepository

cart_repository: CartRepository = SqlCartRepository()
