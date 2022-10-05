from typing import List


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
