from fastapi import FastAPI

app = FastAPI()


@app.get('/web_store_cart/carts')
def get_active_cart():
    pass


@app.post('/web_store_cart/carts')
def create_cart():
    pass


@app.post('/web_store_cart/carts/cart_products')
def add_product_to_cart():
    pass


@app.delete('/web_store_cart/cart_products/{cart_product_id}')
def remove_product_from_cart():
    pass


@app.delete('/web_store_cart/carts')
def clear_cart():
    pass
