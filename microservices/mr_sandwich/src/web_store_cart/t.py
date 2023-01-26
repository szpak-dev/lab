import asyncio
from product.application.update_product import UpdateProductCommand
from shared.command_bus import bus


async def main():
    command = UpdateProductCommand(2, 'dish_updated')
    await bus.handle(command)

asyncio.run(main())
