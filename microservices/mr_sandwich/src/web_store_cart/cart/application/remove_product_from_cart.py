from dataclasses import dataclass

from buslane.commands import Command, CommandHandler

from cart.domain.value_objects import CustomerId, CartProductId
from cart.infrastructure import cart_repository


@dataclass(frozen=True)
class RemoveProductFromCartCommand(Command):
    cart_id: int
    customer_id: int
    cart_product_id: int


class RemoveProductFromCartCommandHandler(CommandHandler[RemoveProductFromCartCommand]):
    def handle(self, command: RemoveProductFromCartCommand) -> None:
        customer_id = CustomerId(command.customer_id)
        cart = cart_repository.get_active_for_customer(customer_id)
        cart.remove_product(CartProductId(command.cart_product_id))
        cart_repository.save(cart)
