import functools
from typing import List, Callable
from abc import ABC, abstractmethod


class ApplicationCommand:
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


class MediatorEvent:
    pass


class MediatorComponent(ABC):
    @abstractmethod
    def on_event(self, event: MediatorEvent):
        pass


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: MediatorComponent, event: MediatorEvent) -> None:
        pass


def docstring_message(cls):
    """Decorates an exception to make its docstring its default message."""
    # Must use cls_init name, not cls.__init__ itself, in closure to avoid recursion
    cls_init = cls.__init__

    @functools.wraps(cls.__init__)
    def wrapped_init(self, msg=cls.__doc__, *args, **kwargs):
        cls_init(self, msg, *args, **kwargs)

    cls.__init__ = wrapped_init
    return cls
