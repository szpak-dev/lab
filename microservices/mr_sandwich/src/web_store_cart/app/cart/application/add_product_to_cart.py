from dataclasses import dataclass
from buslane.commands import Command, CommandHandler

from cart.domain.value_objects import CustomerId
from cart.infrastructure import cart_repository


@dataclass(frozen=True)
class AddProductToCartCommand(Command):
    cart_id: int
    customer_id: int
    product_id: int


class AddProductToCartCommandHandler(CommandHandler[AddProductToCartCommand]):
    def handle(self, command: AddProductToCartCommand) -> None:
        customer_id = CustomerId(command.customer_id)
        cart_repository.get_active_for_customer(customer_id)
