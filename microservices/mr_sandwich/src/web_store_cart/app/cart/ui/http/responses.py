from typing import List
from pydantic import BaseModel


class CartProduct(BaseModel):
    id: int = 1
    product_name: str = 'product name'
    price: float = 7.89


class Cart(BaseModel):
    id: int = 1
    status: str = 'ACTIVE'
    total_price: float = 9.99
    cart_products: List[CartProduct] = []
