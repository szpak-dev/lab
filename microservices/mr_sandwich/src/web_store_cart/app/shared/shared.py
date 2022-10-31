import functools
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import List
from random import randrange
# from kombu import Exchange, Queue, Connection


def docstring_message(cls):
    """Decorates an exception to make its docstring its default message."""
    # Must use cls_init full_name, not cls.__init__ itself, in closure to avoid recursion
    cls_init = cls.__init__

    @functools.wraps(cls.__init__)
    def wrapped_init(self, msg=cls.__doc__, *args, **kwargs):
        cls_init(self, msg, *args, **kwargs)

    cls.__init__ = wrapped_init
    return cls


def generate_number_base64(length: int = 32) -> str:
    ascii_ranges = ((48, 57), (65, 90), (97, 122))
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    steps = range(0, length)

    num = []
    for step in steps:
        character_index = randrange(0, len(chars) - 1)
        num.append(chars[character_index])

    return ''.join(num)


class DomainError(Exception):
    pass


class DomainEvent(ABC):
    def __init__(self, full_name):
        self._bc, self._aggregate, self._name = full_name.split('.')

    def bounded_context(self) -> str:
        return self._bc

    def aggregate(self) -> str:
        return self._aggregate

    def name(self) -> str:
        return self._name

    @abstractmethod
    def serialize(self) -> str:
        pass


class AggregateRoot:
    def __init__(self):
        self._events: List[DomainEvent] = []

    def _emit_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    def release_events(self) -> List[DomainEvent]:
        events = self._events
        self._events = []
        return events


# def emit_events(domain_events: List[DomainEvent]) -> None:
#     with Connection(os.getenv('RABBITMQ_DSN')) as connection:
#         producer = connection.Producer()
#         for event in domain_events:
#             exchange = Exchange(event.bounded_context(), 'direct', durable=True)
#             queue = Queue(event.aggregate(), exchange=exchange, routing_key=event.name())
#             producer.publish(event.serialize(), exchange=exchange, routing_key=event.name(), declare=[queue])


class BaseRepository(ABC):
    pass


class ValueObject(ABC):
    @abstractmethod
    def value(self):
        pass


@dataclass(frozen=True)
class Money:
    value: float
    currency: str = 'ABC'
