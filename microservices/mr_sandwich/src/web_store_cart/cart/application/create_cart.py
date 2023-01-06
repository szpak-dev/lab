from dataclasses import dataclass

from buslane.commands import Command, CommandHandler

from cart.domain.entities import Cart
from cart.domain.erorrs import ActiveCartExists, CartNotFound
from cart.domain.value_objects import CustomerId
from cart.infrastructure import cart_repository


@dataclass(frozen=True)
class CreateCartCommand(Command):
    customer_id: int


class CreateCartCommandHandler(CommandHandler[CreateCartCommand]):
    def handle(self, command: CreateCartCommand) -> None:
        try:
            cart_repository.get_active_for_customer(CustomerId(command.customer_id))
            raise ActiveCartExists
        except CartNotFound:
            pass

        new_cart = Cart()
        new_cart.customer_id = command.customer_id
        new_cart.status = 'ACTIVE'
        new_cart.total_price = 0.0
        cart_repository.save(new_cart)
