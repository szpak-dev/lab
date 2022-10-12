import functools
from abc import ABC
from typing import List
from random import randrange


def docstring_message(cls):
    """Decorates an exception to make its docstring its default message."""
    # Must use cls_init name, not cls.__init__ itself, in closure to avoid recursion
    cls_init = cls.__init__

    @functools.wraps(cls.__init__)
    def wrapped_init(self, msg=cls.__doc__, *args, **kwargs):
        cls_init(self, msg, *args, **kwargs)

    cls.__init__ = wrapped_init
    return cls


def generate_number_base64(length: int = 32) -> str:
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
    steps = range(0, length)

    num = []
    for step in steps:
        character_index = randrange(0, len(chars) - 1)
        num.append(chars[character_index])

    return ''.join(num)


class DomainError(Exception):
    pass


class DomainEvent:
    def __init__(self, name):
        self.name = name


class AggregateRoot:
    def __init__(self):
        self._events: List[DomainEvent] = []

    def emit_event(self, event: DomainEvent) -> None:
        self._events.append(event)

    def release_events(self) -> List[DomainEvent]:
        events = self._events
        self._events = []
        return events


class BaseRepository(ABC):
    pass
