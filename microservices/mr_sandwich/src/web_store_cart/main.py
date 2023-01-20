from __future__ import annotations

from typing import List

from fastapi import FastAPI, HTTPException
from logger import logging

from cart.domain.erorrs import CartNotFound, ActiveCartExists, ProductNotInCart
from cart.ui.http import controllers as cart_controllers
from product.ui.http import controllers as product_controllers
from cart.ui.http.responses import Cart
from product.ui.http.responses import ProductListItem, Product
from cart.ui.http.requests import AddProductToCart

logging.info('Starting web_store_cart application')

app = FastAPI(debug=True)


@app.on_event('startup')
async def on_startup():
    pass


@app.get('/web_store_cart/carts', status_code=200, response_model=Cart, tags=['Cart'])
async def get_active_cart(customer_id: int) -> Cart:
    try:
        return await cart_controllers.get_active_cart(customer_id)
    except CartNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.post('/web_store_cart/carts', status_code=201, tags=['Cart'])
async def create_cart(customer_id: int):
    try:
        await cart_controllers.create_cart(customer_id)
    except ActiveCartExists as e:
        raise HTTPException(status_code=409, detail=str(e))


@app.post('/web_store_cart/carts/{cart_id}/cart_products', status_code=201, tags=['Cart'])
async def add_product_to_cart(cart_id: int, product: AddProductToCart, customer_id: int):
    try:
        await cart_controllers.add_product_to_cart(
            cart_id,
            customer_id,
            product.product_id,
        )
    except CartNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.delete('/web_store_cart/carts/{cart_id}/cart_products/{cart_product_id}', status_code=204, tags=['Cart'])
async def remove_product_from_cart(cart_id: int, cart_product_id: int, customer_id: int):
    try:
        await cart_controllers.remove_product_from_cart(
            cart_id,
            customer_id,
            cart_product_id,
        )
    except (CartNotFound, ProductNotInCart) as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.delete('/web_store_cart/carts/{cart_id}', status_code=204, tags=['Cart'])
async def clear_cart(cart_id: int, customer_id: int):
    try:
        await cart_controllers.clear_cart(cart_id, customer_id)
    except CartNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get('/web_store_cart/products', status_code=200, response_model=List[ProductListItem], tags=['Product'])
def get_products_list():
    return product_controllers.get_product_list()


@app.get('/web_store_cart/products/{product_id}', status_code=200, response_model=Product, tags=['Product'])
def get_product():
    return product_controllers.get_product(1)
