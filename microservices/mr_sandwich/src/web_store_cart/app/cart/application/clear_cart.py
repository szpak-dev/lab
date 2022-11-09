from dataclasses import dataclass

from buslane.commands import Command, CommandHandler


@dataclass(frozen=True)
class ClearCartCommand(Command):
    cart_id: int
    customer_id: int


class ClearCartCommandHandler(CommandHandler[ClearCartCommand]):
    def handle(self, command: ClearCartCommand) -> None:
        pass
