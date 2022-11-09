from dataclasses import dataclass

from buslane.commands import Command, CommandHandler


@dataclass(frozen=True)
class CreateCartCommand(Command):
    customer_id: int


class CreateCartCommandHandler(CommandHandler[CreateCartCommand]):
    def handle(self, command: CreateCartCommand) -> None:
        pass
