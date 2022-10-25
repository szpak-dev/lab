from dataclasses import dataclass

from buslane.commands import Command, CommandHandler

from cart.domain.value_objects import CustomerId


@dataclass(frozen=True)
class CreateCartCommand(Command):
    customer_id: CustomerId


class CreateCartCommandHandler(CommandHandler[CreateCartCommand]):
    def handle(self, command: CreateCartCommand) -> None:
        pass
