from app.mediator import MediatorComponent
from app.user.adapters import credentials_checker
from app.mediator.bus_event import BusEvent


class UserModule(MediatorComponent):
    def on_authorization_started(self, data):
        username, password = data
        credentials_checker.check(username, password)

        self.emit_credentials_confirmed(username)

    def emit_credentials_confirmed(self, username: str):
        self.mediator.notify(self, BusEvent.CREDENTIALS_CONFIRMED, [username])
