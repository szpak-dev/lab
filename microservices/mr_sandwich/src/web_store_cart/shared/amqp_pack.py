import asyncio
from abc import ABC, abstractmethod
from dataclasses import dataclass
from json import loads
from typing import Any

from aio_pika import connect, ExchangeType
from aio_pika.abc import AbstractIncomingMessage
from aio_pika.abc import AbstractQueue
from aio_pika.abc import AbstractExchange
from aio_pika.abc import AbstractChannel
from aio_pika.abc import AbstractConnection

from config import settings


class AmqpConsumerError(BaseException):
    ...


@dataclass(frozen=True)
class AmqpQueueDefinition:
    name: str
    routing_keys: list[str]
    durable: bool = True


@dataclass(frozen=True)
class AmqpExchangeDefinition:
    name: str
    queues: list[AmqpQueueDefinition]
    type: ExchangeType = ExchangeType.DIRECT
    durable: bool = True


@dataclass(frozen=True)
class AmqpChannel:
    number: int
    exchanges: list[AmqpExchangeDefinition]


@dataclass(frozen=True)
class AmqpConnection:
    dsn: str
    channel: AmqpChannel | None = None


class AmqpConsumer:
    def __init__(self, dsn: str):
        self._dsn = dsn
        self._exchange_definitions: dict[str, AmqpExchangeDefinition] = {}
        self._queue_definitions: dict[str, AmqpQueueDefinition] = {}
        self._exchange_definition_context: AmqpExchangeDefinition | None = None

    def in_exchange(self, name: str):
        self._exchange_definitions[name] = AmqpExchangeDefinition(name, [])
        self._exchange_definition_context = self._exchange_definitions[name]

    def will_have_a_queue(self, name: str, routing_keys: list[str]) -> None:
        if self._exchange_definition_context is None:
            raise AmqpConsumerError(f'Exchange context is missing, did you call with_exchange() method?')

        self._queue_definitions[name] = AmqpQueueDefinition(name, routing_keys)
        self._exchange_definition_context.queues.append(self._queue_definitions[name])

    def get_connection(self) -> AmqpConnection:
        channel = AmqpChannel(1, [])
        for exchange_name, exchange_definition in self._exchange_definitions.items():
            channel.exchanges.append(exchange_definition)

        connection: AmqpConnection = AmqpConnection(self._dsn, channel)
        return connection


class AmqpConsumerAdapter(ABC):
    @abstractmethod
    async def connect(self) -> list[Any]:
        ...

    @abstractmethod
    async def consume(self, queues: list[Any], callback: callable):
        ...


class AioPikaAsyncConsumer(AmqpConsumerAdapter):
    def __init__(self, connection: AmqpConnection):
        self._connection = connection

    async def connect(self) -> list[AbstractQueue]:
        async def create_connection() -> AbstractConnection:
            connection = await connect(self._connection.dsn)
            return connection

        async def create_channel(amqp_connection: AbstractConnection) -> AbstractChannel:
            amqp_channel = await amqp_connection.channel()
            await amqp_channel.set_qos(prefetch_count=1)
            return amqp_channel

        async def create_queues(amqp_channel: AbstractChannel) -> list[AbstractQueue]:
            exchanges: list[AbstractExchange] = []
            queues: list[AbstractQueue] = []

            definition: AmqpExchangeDefinition
            for definition in self._connection.channel.exchanges:
                exchange: AbstractExchange = await amqp_channel.declare_exchange(
                    name=definition.name,
                    type=definition.type,
                    durable=definition.durable
                )

                exchanges.append(exchange)

                query_definition: AmqpQueueDefinition
                for query_definition in definition.queues:
                    queue: AbstractQueue = await amqp_channel.declare_queue(
                        name=query_definition.name,
                        durable=query_definition.durable,
                    )

                    for key in query_definition.routing_keys:
                        await queue.bind(exchange=exchange, routing_key=key)

                    queues.append(queue)

            return queues

        aio_pika_connection = await create_connection()
        aio_pika_channel = await create_channel(aio_pika_connection)
        aio_pika_queues = await create_queues(aio_pika_channel)
        return aio_pika_queues

    async def consume(self, aio_pika_queues: list[AbstractQueue], cb) -> None:
        for queue in aio_pika_queues:
            async with queue.iterator() as iterator:
                message: AbstractIncomingMessage
                async for message in iterator:
                    await cb(message)

            await asyncio.Future()


async def main():
    async def process_message(message: AbstractIncomingMessage) -> None:
        async with message.process(requeue=True):
            dish_id = loads(message.body)[0]
            operation_type = message.routing_key
            print(dish_id, operation_type)

    consumer = AmqpConsumer(settings['RABBITMQ_DSN'])
    consumer.in_exchange('food_factory')
    consumer.will_have_a_queue('dishes', ['dish_created', 'dish_updated', 'dish_removed'])

    consumer.in_exchange('auth')
    consumer.will_have_a_queue('users', ['user_promoted', 'user_demoted'])
    consumer.will_have_a_queue('authentications', ['success', 'failed'])

    aio_pika_consumer: AmqpConsumerAdapter = AioPikaAsyncConsumer(consumer.get_connection())
    aio_pika_queues = await aio_pika_consumer.connect()
    await aio_pika_consumer.consume(aio_pika_queues, process_message)


if __name__ == "__main__":
    asyncio.run(main())
