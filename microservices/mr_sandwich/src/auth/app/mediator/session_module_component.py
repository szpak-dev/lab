from app.mediator import MediatorComponent
from app.session.adapters import session_repository
from app.session.domain.value_objects import Credentials
from app.mediator.bus_event import BusEvent


class SessionModule(MediatorComponent):
    def emit_authorization_started(self, credentials: Credentials):
        username, plain_password = credentials.username, credentials.password
        self.mediator.notify(self, BusEvent.AUTHENTICATION_STARTED, [username, plain_password])

    def on_credentials_confirmed(self, username: str):
        session_repository.save(username)
        self.mediator.notify(self, BusEvent.CREDENTIALS_CONFIRMED)
