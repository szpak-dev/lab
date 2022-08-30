from aggregate_root import AggregateRoot
from cart_events import ProductAddedToCart, ProductRemovedFromCart


class Cart(AggregateRoot):
    """Method handles adding Product to the Cart and emits ProductAddedToCart event"""
    def add_product(self, product_id):
        event = ProductAddedToCart(product_id)
        self.record_event(event)
        pass

    """Method handles removing Product from the Cart and emits ProductRemovedFromCart event"""
    def remove_product(self, product_id):
        event = ProductRemovedFromCart(product_id)
        self.record_event(event)
        pass
