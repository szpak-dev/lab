import asyncio

from aio_pika import DeliveryMode, ExchangeType, Message, connect
from aio_pika.abc import AbstractIncomingMessage

from shared.config import settings


async def main() -> None:
    connection = await connect(settings['RABBITMQ_DSN'])

    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=1)

        exchange = await channel.declare_exchange('food_factory', ExchangeType.DIRECT)
        queue = await channel.declare_queue(name='products')

        await queue.bind(exchange, routing_key='product_created')
        await queue.bind(exchange, routing_key='product_updated')

        async with queue.iterator() as iterator:
            message: AbstractIncomingMessage
            async for message in iterator:
                async with message.process():
                    print(f'{message.routing_key}:{message.body}')

        print('waiting for messages...')
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
