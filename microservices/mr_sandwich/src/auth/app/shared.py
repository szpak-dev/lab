from typing import List, Callable
import functools
from dataclasses import dataclass, field


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


@dataclass
class Observable:
    observers: List[Callable] = field(default_factory=list)

    def register(self, observer: Callable):
        self.observers.append(observer)

    def deregister(self, observer: Callable):
        self.observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self.observers:
            observer(*args, **kwargs)


def docstring_message(cls):
    """Decorates an exception to make its docstring its default message."""
    # Must use cls_init name, not cls.__init__ itself, in closure to avoid recursion
    cls_init = cls.__init__

    @functools.wraps(cls.__init__)
    def wrapped_init(self, msg=cls.__doc__, *args, **kwargs):
        cls_init(self, msg, *args, **kwargs)

    cls.__init__ = wrapped_init
    return cls
