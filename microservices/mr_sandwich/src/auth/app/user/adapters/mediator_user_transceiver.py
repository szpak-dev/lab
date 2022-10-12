from app.mediator import MediatorComponent, Mediator
from app.mediator.bus_event import BusEvent
from app.user.domain.ports.credentials_checker import CredentialsChecker
from app.user.domain.ports.user_transceiver import UserTransceiver


class MediatorUserTransceiver(UserTransceiver, MediatorComponent):
    def __init__(self, mediator: Mediator, credentials_checker: CredentialsChecker):
        super().__init__(mediator)
        self._credentials_checker = credentials_checker

    def on_authentication_started(self, data):
        username, password = data
        self._credentials_checker.check(username, password)
        self.emit_credentials_confirmed(username)

    def emit_credentials_confirmed(self, username: str):
        self.mediator.notify(self, BusEvent.CREDENTIALS_CONFIRMED, [username])
