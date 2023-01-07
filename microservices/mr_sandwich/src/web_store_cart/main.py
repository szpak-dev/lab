from os import getenv
from typing import List

from fastapi import FastAPI, HTTPException, Form
from uvicorn import run

from cart.domain.erorrs import CartNotFound, ActiveCartExists
from cart.ui.http import controllers as cart_controllers
from product.ui.http import controllers as product_controllers
from cart.ui.http.responses import Cart
from product.ui.http.responses import ProductListItem, Product

app = FastAPI()


@app.get('/web_store_cart/carts', status_code=200, response_model=Cart, tags=['Cart'])
def get_active_cart(customer_id: int) -> Cart:
    try:
        return cart_controllers.get_active_cart(customer_id)
    except CartNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post('/web_store_cart/carts', status_code=201, tags=['Cart'])
def create_cart(customer_id: int = Form()):
    try:
        return cart_controllers.create_cart(customer_id)
    except ActiveCartExists as e:
        raise HTTPException(status_code=409, detail=str(e))


@app.post('/web_store_cart/carts/{cart_id}/cart_products', status_code=201, tags=['Cart'])
def add_product_to_cart(cart_id: int, customer_id: int = Form(), product_id: int = Form()):
    try:
        cart_controllers.add_product_to_cart(
            cart_id,
            customer_id,
            product_id,
        )
    except CartNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.delete('/web_store_cart/carts/{cart_id}/cart_products/{cart_product_id}', status_code=204, tags=['Cart'])
def remove_product_from_cart(cart_id: int, cart_product_id: int, customer_id: int):
    try:
        return cart_controllers.remove_product_from_cart(
            cart_id,
            customer_id,
            cart_product_id,
        )
    except CartNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.delete('/web_store_cart/carts/{cart_id}', status_code=204, tags=['Cart'])
def clear_cart(cart_id: int, customer_id: int):
    try:
        return cart_controllers.clear_cart(cart_id, customer_id)
    except CartNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get('/web_store_cart/products', status_code=200, response_model=List[ProductListItem], tags=['Product'])
def get_products_list():
    return product_controllers.get_product_list()


@app.get('/web_store_cart/products/{product_id}', status_code=200, response_model=Product, tags=['Product'])
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
