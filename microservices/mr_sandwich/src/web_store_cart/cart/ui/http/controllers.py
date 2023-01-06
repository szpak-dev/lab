from cart.application import command_bus
from cart.application.add_product_to_cart import AddProductToCartCommand
from cart.application.clear_cart import ClearCartCommand
from cart.application.create_cart import CreateCartCommand
from cart.application.remove_product_from_cart import RemoveProductFromCartCommand
from cart.application.get_active_cart import provide
from cart.ui.http.responses import Cart


def get_active_cart(customer_id: int) -> Cart:
    return provide(customer_id)


def create_cart(customer_id: int) -> None:
    command_bus.execute(CreateCartCommand(customer_id))


def add_product_to_cart(cart_id: int, customer_id: int, product_id: int) -> None:
    command_bus.execute(AddProductToCartCommand(
        cart_id,
        customer_id,
        product_id,
    ))


def remove_product_from_cart(cart_id: int, customer_id: int, cart_product_id: int) -> None:
    command_bus.execute(RemoveProductFromCartCommand(
        cart_id,
        customer_id,
        cart_product_id,
    ))


def clear_cart(cart_id: int, customer_id: int) -> None:
    command_bus.execute(ClearCartCommand(
        cart_id,
        customer_id,
    ))
