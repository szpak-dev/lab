import asyncio
from json import loads

from aio_pika import DeliveryMode, ExchangeType, Message, connect
from aio_pika.abc import AbstractIncomingMessage

from shared.config import settings
from shared.command_bus import bus
from product.application.update_product import UpdateProductCommand


async def main() -> None:
    connection = await connect(settings['RABBITMQ_DSN'])

    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        exchange = await channel.declare_exchange('food_factory', ExchangeType.DIRECT)
        queue = await channel.declare_queue(name='dishes')

        await queue.bind(exchange, routing_key='dish_created')
        await queue.bind(exchange, routing_key='dish_updated')
        await queue.bind(exchange, routing_key='dish_removed')

        async with queue.iterator() as iterator:
            message: AbstractIncomingMessage
            async for message in iterator:
                async with message.process():
                    dish_id = loads(message.body)[0]
                    operation_type = message.routing_key
                    await bus.handle(UpdateProductCommand(dish_id, operation_type))

        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
