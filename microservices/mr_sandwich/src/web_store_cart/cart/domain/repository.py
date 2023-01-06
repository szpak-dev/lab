from abc import ABC, abstractmethod

from cart.domain.entities import Cart
from cart.domain.value_objects import CustomerId


class CartRepository(ABC):
    @abstractmethod
    def get_active_for_customer(self, customer_id: CustomerId) -> Cart:
        pass

    @abstractmethod
    def save(self, cart: Cart) -> None:
        pass
