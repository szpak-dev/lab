from cart_events import ProductAddedToCart, ProductRemovedFromCart


class AbandonedCarts:
    def add_cart_operation(self, cart_id):
        """Bump last action timestamp on the Cart"""
        pass

    def get_abandoned(self):
        """Fetch all abandoned carts by whatever conditions"""
        pass


class CartListener:
    """Listens for Product changes in Cart, communicates with Abandoned Carts system"""
    def on_product_added(self, event: ProductAddedToCart):
        AbandonedCarts.add_cart_operation(event.get_data('cart_id'))
        pass

    def on_product_removed(self, event: ProductRemovedFromCart):
        AbandonedCarts.add_cart_operation(event.get_data('cart_id'))
        pass
