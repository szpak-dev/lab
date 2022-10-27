from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship

from cart.domain.events import ProductAddedToCart, ProductRemovedFromCart, CartCleared
from cart.domain.value_objects import CartProductId
from shared.db import Base
from shared.shared import AggregateRoot, Money


class Cart(Base, AggregateRoot):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True)
    cart_products = relationship('CartProduct', back_populates='cart')
    customer_id = Column(Integer)
    status = Column(String)
    total_price = Column(Float)
    created_at = Column(DateTime, default=datetime.now)

    def add_product(self, product_id: int, name: str, price: Money) -> None:
        self._emit_event(ProductAddedToCart())

    def remove_product(self, cart_product_id: CartProductId):
        self._emit_event(ProductRemovedFromCart())

    def clear(self):
        self._emit_event(CartCleared())


class CartProduct(Base):
    __tablename__ = 'cart_products'

    id = Column(Integer, primary_key=True)
    cart = relationship('Cart', back_populates='cart_products')
    product_id = Column(Integer)
    product_name = Column(String)
    price = Column(Float)
    created_at = Column(DateTime, default=datetime.now)



