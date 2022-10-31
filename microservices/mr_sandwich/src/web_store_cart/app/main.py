from os import getenv
from typing import List

from fastapi import FastAPI
from uvicorn import run

# Use aliases only in bootstrapping file, on deeper levels it may mess up IDE auto refactor result.
from cart.ui.http import controllers as cart_controllers
from product.ui.http import controllers as product_controllers
from cart.ui.http.responses import Cart
from product.ui.http.responses import ProductListItem, Product

app = FastAPI()


@app.get(
    '/web_store_cart/carts',
    status_code=200,
    response_model=Cart,
    tags=['Cart'],
)
def get_active_cart() -> Cart:
    return cart_controllers.get_active_cart(1)


@app.post(
    '/web_store_cart/carts',
    status_code=201,
    tags=['Cart'],
)
def create_cart():
    return cart_controllers.create_cart(1)


@app.post(
    '/web_store_cart/carts/cart_products',
    status_code=201,
    tags=['Cart'],
)
def add_product_to_cart():
    return cart_controllers.add_product_to_cart(1, 1, 1)


@app.delete(
    '/web_store_cart/carts/cart_products/{cart_product_id}',
    status_code=204,
    tags=['Cart'],
)
def remove_product_from_cart(cart_product_id):
    return cart_controllers.remove_product_from_cart(1, 1, 1)


@app.delete(
    '/web_store_cart/carts',
    status_code=204,
    tags=['Cart'],
)
def clear_cart():
    return cart_controllers.clear_cart(1, 1)


@app.get(
    '/web_store_cart/products',
    status_code=200,
    response_model=List[ProductListItem],
    tags=['Product'],
)
def get_products_list():
    return product_controllers.get_product_list()


@app.get(
    '/web_store_cart/products/{product_id}',
    status_code=200,
    response_model=Product,
    tags=['Product'],
)
def get_product():
    return product_controllers.get_product(1)


if __name__ == "__main__":
    run(
        app,
        host="0.0.0.0",
        port=80,
        log_level=getenv('WSGI_LOG_LEVEL'),
        proxy_headers=True,
        workers=1,
        access_log=False,
    )
