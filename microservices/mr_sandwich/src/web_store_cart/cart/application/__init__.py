from buslane.commands import CommandBus

from cart.application.add_product_to_cart import AddProductToCartCommandHandler
from cart.application.clear_cart import ClearCartCommandHandler
from cart.application.create_cart import CreateCartCommandHandler
from cart.application.remove_product_from_cart import RemoveProductFromCartCommandHandler

command_bus = CommandBus()
command_bus.register(handler=AddProductToCartCommandHandler())
command_bus.register(handler=ClearCartCommandHandler())
command_bus.register(handler=CreateCartCommandHandler())
command_bus.register(handler=RemoveProductFromCartCommandHandler())
