from dataclasses import dataclass

from buslane.commands import Command, CommandHandler

from cart.domain.value_objects import CustomerId, CartId


@dataclass(frozen=True)
class ClearCartCommand(Command):
    cart_id: CartId
    customer_id: CustomerId


class ClearCartCommandHandler(CommandHandler[ClearCartCommand]):
    def handle(self, command: ClearCartCommand) -> None:
        pass
