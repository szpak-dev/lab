import asyncio
from json import loads
from typing import List

from aio_pika import ExchangeType, connect
from aio_pika.abc import AbstractIncomingMessage, AbstractQueue, AbstractExchange, AbstractConnection, AbstractChannel
from aio_pika.patterns import NackMessage

from product.domain.erorrs import ProductError
from shared.config import settings
from shared.command_bus import bus
from shared.logger import logging
from product.application.update_product import UpdateProductCommand


async def create_channel(connection: AbstractConnection) -> AbstractChannel:
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)
    return channel


async def declare_exchange_and_queue(channel: AbstractChannel, exchange_name: str, queue_name: str):
    exchange = await channel.declare_exchange(exchange_name, ExchangeType.DIRECT, durable=True)
    queue = await channel.declare_queue(name=queue_name, durable=True)
    return exchange, queue


async def bind_routing_keys(exchange: AbstractExchange, queue: AbstractQueue, routing_keys: List[str]) -> None:
    for key in routing_keys:
        await queue.bind(exchange, routing_key=key)


async def process_message(message: AbstractIncomingMessage) -> None:
    async with message.process(requeue=True):
        dish_id = loads(message.body)[0]
        operation_type = message.routing_key
        try:
            await bus.handle(UpdateProductCommand(dish_id, operation_type))
            logging.debug(f'Product change operation executed: ({operation_type}, {dish_id})')
        except ProductError as e:
            logging.error(str(e))
            raise NackMessage


async def main() -> None:
    connection = await connect(settings['RABBITMQ_DSN'])

    async with connection:
        channel = await create_channel(connection)
        exchange, queue = await declare_exchange_and_queue(channel, 'food_factory', 'dishes')

        routing_keys = ['dish_created', 'dish_updated', 'dish_removed']
        await bind_routing_keys(exchange, queue, routing_keys)

        async with queue.iterator() as iterator:
            message: AbstractIncomingMessage
            async for message in iterator:
                await process_message(message)

        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
