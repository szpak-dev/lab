class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price


class CartProduct:
    def __init__(self, product_id, name, price):
        self._product_id = product_id
        self._name = name
        self._price = price

    def is_promoted(self):
        return False


class Cart:
    def __init__(self):
        self._total_value = 0
        self._cart_products = []
        self._cart_promotions = []

    def add_product(self, product: Product):
        if len(self._cart_products) == 50:
            raise Exception("Too many products in cart")

        cart_product = CartProduct(product.id, product.name, product.price)
        self._cart_products.append(cart_product)

        pass

    def remove_product(self, cart_product_id):
        pass


class CartVersioned(Cart):
    def __init__(self):
        super().__init__()
        self._version = 0

    def get_version(self):
        return self._version
