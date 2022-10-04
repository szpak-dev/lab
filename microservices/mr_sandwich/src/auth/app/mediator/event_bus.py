from dataclasses import dataclass

from app.shared import Mediator, MediatorComponent, MediatorEvent
from app.mediator.session_module_component import SessionModule
from app.mediator.user_module_component import UserModule


@dataclass
class EventBus(Mediator):
    def __init__(self):
        self.user_module = UserModule(event_bus=self)
        self.session_module = SessionModule(event_bus=self)

    def notify(self, sender: MediatorComponent, event: MediatorEvent) -> None:
        if isinstance(sender, SessionModule):
            self.user_module.on_event(event)

        if isinstance(sender, UserModule):
            self.session_module.on_event(event)


__bus = []


def event_bus_factory() -> EventBus:
    if __bus.count == 0:
        __bus.append(EventBus())

    return __bus[0]
