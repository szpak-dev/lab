from dataclasses import dataclass

from cart.domain.value_objects import CustomerId
from command_coach.command import CommandHandler, Command
from cart.infrastructure import cart_repository


@dataclass(frozen=True)
class TestCommand(Command):
    prop_one: str


class TestCommandHandler(CommandHandler):
    async def handle(self, command: TestCommand):
        cart = await cart_repository.get_active_for_customer(CustomerId(4))
        await cart_repository.save(cart)
