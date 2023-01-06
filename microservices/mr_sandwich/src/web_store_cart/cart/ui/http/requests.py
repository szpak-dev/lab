from pydantic import BaseModel


class AddProductToCart(BaseModel):
    customer_id: int
    product_id: int
