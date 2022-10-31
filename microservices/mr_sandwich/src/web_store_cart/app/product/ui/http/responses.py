from typing import List
from pydantic import BaseModel


class Product(BaseModel):
    name: str = 'Product'
    description: str = 'Description'
    price: float = 0.11
    ingredients: List[str] = ['ingredient']
    weight: float = 12.978


class ProductListItem(BaseModel):
    name: str = 'Product List Item'
    price: float = 1.22
