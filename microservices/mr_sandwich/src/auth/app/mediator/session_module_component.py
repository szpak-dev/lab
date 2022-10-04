from app.shared import MediatorComponent, MediatorEvent
from app.session.adapters import session_repository
from app.mediator.events import CredentialsConfirmed, AuthenticationSuccessful


class SessionModule(MediatorComponent):
    def __init__(self, event_bus):
        self._event_bus = event_bus

    def on_event(self, event: MediatorEvent):
        if isinstance(event, CredentialsConfirmed):
            session_repository().save(event.username)
            return self._event_bus.notify(self, AuthenticationSuccessful())
