from domain_event import DomainEvent


class AggregateRoot:
    """List of Domain Events which will be dispatched after successful DBMS transaction, the Aggregate was a part of"""
    _recorded_events = []

    def record_event(self, domain_event: DomainEvent):
        self._recorded_events.append(domain_event)

    def drain_events(self):
        """Method has to make sure that released Events are not left in the memory"""
        events = self._recorded_events
        self._recorded_events = []

        return events
