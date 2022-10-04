from app.shared import MediatorComponent, MediatorEvent
from app.user.adapters import UserCredentialsChecker
from app.mediator.events import AuthenticationStarted, AuthenticationSuccessful, CredentialsConfirmed


class UserModule(MediatorComponent):
    def __init__(self, event_bus):
        self._event_bus = event_bus

    def on_event(self, event: MediatorEvent):
        if isinstance(event, AuthenticationStarted):
            UserCredentialsChecker().check(event.username, event.password)
            return self._event_bus.notify(self, CredentialsConfirmed(event.username))
