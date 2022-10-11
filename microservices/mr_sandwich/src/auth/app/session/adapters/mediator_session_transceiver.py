from app.session.domain.value_objects import Credentials
from app.mediator.bus_event import BusEvent
from app.mediator import MediatorComponent, Mediator
from app.session.domain.ports.session_repository import SessionRepository
from app.session.domain.ports.session_transceiver import SessionTransceiver


class MediatorSessionTransceiver(SessionTransceiver, MediatorComponent):
    def __init__(self, mediator: Mediator, session_repository: SessionRepository):
        super().__init__(mediator)
        self._session_repository = session_repository

    def emit_authentication_started(self, credentials: Credentials):
        username, plain_password = credentials.username, credentials.password
        self.mediator.notify(self, BusEvent.AUTHENTICATION_STARTED, [username, plain_password])

    def on_credentials_confirmed(self, username: str):
        self._session_repository.save(username)
        self.mediator.notify(self, BusEvent.AUTHENTICATION_SUCCESSFUL, [username])
