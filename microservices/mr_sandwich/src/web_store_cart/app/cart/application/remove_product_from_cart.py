from dataclasses import dataclass

from buslane.commands import Command, CommandHandler

from cart.domain.value_objects import CartId, CustomerId, CartProductId


@dataclass(frozen=True)
class RemoveProductFromCartCommand(Command):
    cart_id: CartId
    customer_id: CustomerId
    cart_product_id: CartProductId


class RemoveProductFromCartCommandHandler(CommandHandler[RemoveProductFromCartCommand]):
    def handle(self, command: RemoveProductFromCartCommand) -> None:
        pass
