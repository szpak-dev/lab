from dataclasses import dataclass

from buslane.commands import Command, CommandHandler

from cart.domain.value_objects import CustomerId
from cart.infrastructure import cart_repository


@dataclass(frozen=True)
class ClearCartCommand(Command):
    cart_id: int
    customer_id: int


class ClearCartCommandHandler(CommandHandler[ClearCartCommand]):
    def handle(self, command: ClearCartCommand) -> None:
        customer_id = CustomerId(command.customer_id)
        cart = cart_repository.get_active_for_customer(customer_id)
        cart.clear()
        cart_repository.save(cart)
