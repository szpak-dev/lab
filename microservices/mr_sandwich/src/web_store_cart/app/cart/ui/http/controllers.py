from cart.application import command_bus
from cart.application.add_product_to_cart import AddProductToCartCommand
from cart.application.clear_cart import ClearCartCommand
from cart.application.create_cart import CreateCartCommand
from cart.application.remove_product_from_cart import RemoveProductFromCartCommand
from cart.ui.http.responses import Cart, CartProduct
from cart.domain.value_objects import CustomerId, CartId, CartProductId
from cart.infrastructure.in_memory_cart_repository import repository


def get_active_cart(customer_id: int) -> Cart:
    repository.get_active_for_customer(CustomerId(customer_id))
    return Cart(cart_products=[CartProduct()])


def create_cart(customer_id: int) -> None:
    command_bus.execute(CreateCartCommand(CustomerId(customer_id)))


def add_product_to_cart(cart_id: int, customer_id: int, product_id: int) -> None:
    command_bus.execute(AddProductToCartCommand(
        CartId(cart_id),
        CustomerId(customer_id),
        product_id,
    ))


def remove_product_from_cart(cart_id: int, customer_id: int, cart_product_id: int) -> None:
    command_bus.execute(RemoveProductFromCartCommand(
        CartId(cart_id),
        CustomerId(customer_id),
        CartProductId(cart_product_id),
    ))


def clear_cart(cart_id: int, customer_id: int) -> None:
    command_bus.execute(ClearCartCommand(
        CartId(cart_id),
        CustomerId(customer_id),
    ))
