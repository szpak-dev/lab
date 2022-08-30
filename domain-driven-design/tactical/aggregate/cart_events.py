from domain_event import DomainEvent


class ProductAddedToCart(DomainEvent):
    """Dispatched when Product was added to the Cart"""
    def __init__(self, cart_id, product_id):
        data = {cart_id: cart_id, product_id: product_id}
        super().__init__('cart.products.product_added_event', data)


class ProductRemovedFromCart(DomainEvent):
    """Dispatched after the Product was removed from Cart"""
    def __init__(self, cart_id, product_id):
        data = {cart_id: cart_id, product_id: product_id}
        super().__init__('cart.products.product_removed_event', data)
