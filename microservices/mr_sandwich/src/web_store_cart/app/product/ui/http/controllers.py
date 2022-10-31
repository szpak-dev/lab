from typing import List

from product.ui.http.responses import Product, ProductListItem


def get_product_list() -> List[ProductListItem]:
    return [
        ProductListItem(),
        ProductListItem(),
        ProductListItem(),
    ]


def get_product(product_id: int) -> Product:
    return Product()

