from dataclasses import dataclass
from buslane.commands import Command, CommandHandler

from cart.domain.value_objects import CartId, CustomerId
from cart.infrastructure import cart_repository


@dataclass(frozen=True)
class AddProductToCartCommand(Command):
    cart_id: CartId
    customer_id: CustomerId
    product_id: int


class AddProductToCartCommandHandler(CommandHandler[AddProductToCartCommand]):
    def handle(self, command: AddProductToCartCommand) -> None:
        cart_repository.get_active_for_customer(customer_id=command.customer_id)
