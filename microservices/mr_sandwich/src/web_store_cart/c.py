import asyncio

from cart.application import command_bus
from cart.application.test import TestCommand


async def main():
    command = TestCommand(prop_one='1')
    await command_bus.handle(command)


asyncio.run(main())
