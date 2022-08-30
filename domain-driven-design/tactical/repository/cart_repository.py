from abc import ABC, abstractmethod
from sql_repository import SqlRepository


class CartRepository(ABC, SqlRepository):
    """Interface class for Repository managing Carts"""
    @abstractmethod
    def get_user_active_cart(self, user_id):
        pass


class _SqlCartRepository(CartRepository):
    """Interface implementation which de facto must be hidden"""
    def get_user_active_cart(self, user_id):
        return self.query_runner.run(user_id)


def get_cart_repository() -> CartRepository:
    """Fetching Repository by its interface base class, not one implementing it"""
    return _SqlCartRepository()
