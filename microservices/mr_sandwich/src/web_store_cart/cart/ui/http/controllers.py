from shared.command_bus import bus
from cart.application.add_product_to_cart import AddProductToCartCommand
from cart.application.clear_cart import ClearCartCommand
from cart.application.create_cart import CreateCartCommand
from cart.application.remove_product_from_cart import RemoveProductFromCartCommand
from cart.application.get_active_cart import provide
from cart.ui.http.responses import Cart


async def get_active_cart(customer_id: int) -> Cart:
    return await provide(customer_id)


async def create_cart(customer_id: int) -> None:
    await bus.handle(CreateCartCommand(customer_id))


async def add_product_to_cart(cart_id: int, customer_id: int, product_id: int) -> None:
    await bus.handle(AddProductToCartCommand(
        cart_id,
        customer_id,
        product_id,
    ))


async def remove_product_from_cart(cart_id: int, customer_id: int, cart_product_id: int) -> None:
    await bus.handle(RemoveProductFromCartCommand(
        cart_id,
        customer_id,
        cart_product_id,
    ))


async def clear_cart(cart_id: int, customer_id: int) -> None:
    await bus.handle(ClearCartCommand(
        cart_id,
        customer_id,
    ))
