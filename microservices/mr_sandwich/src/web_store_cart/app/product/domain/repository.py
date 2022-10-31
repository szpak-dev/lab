from abc import ABC, abstractmethod

from product.domain.entities import Product
from product.domain.value_objects import ProductId


class ProductRepository(ABC):
    @abstractmethod
    def get(self, product_id: ProductId) -> Product:
        pass

    @abstractmethod
    def save(self, product: Product) -> None:
        pass
