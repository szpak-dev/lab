from dataclasses import dataclass

from buslane.commands import Command, CommandHandler


@dataclass(frozen=True)
class RemoveProductFromCartCommand(Command):
    cart_id: int
    customer_id: int
    cart_product_id: int


class RemoveProductFromCartCommandHandler(CommandHandler[RemoveProductFromCartCommand]):
    def handle(self, command: RemoveProductFromCartCommand) -> None:
        pass
