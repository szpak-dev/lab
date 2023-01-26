from json import dumps
from os import getenv

from pika import URLParameters, BlockingConnection
from pika.exchange_type import ExchangeType

RABBITMQ_DSN = getenv('RABBITMQ_DSN', 'amqp://guest:guest@localhost:5672/')

parameters = URLParameters(RABBITMQ_DSN)
connection = BlockingConnection(parameters)

channel = connection.channel()
channel.exchange_declare('food_factory', ExchangeType.direct)


def publish_dish_created(product_id: int):
    channel.basic_publish(
        routing_key='dish_created',
        exchange='food_factory',
        body=dumps([product_id]),
    )


def publish_dish_updated(product_id: int):
    channel.basic_publish(
        routing_key='dish_updated',
        exchange='food_factory',
        body=dumps([product_id]),
    )


def publish_dish_removed(product_id: int):
    channel.basic_publish(
        routing_key='dish_removed',
        exchange='food_factory',
        body=dumps([product_id]),
    )
