from typing import List

from app.mediator import Mediator, MediatorComponent
from app.mediator.session_module_component import SessionModule
from app.mediator.user_module_component import UserModule
from app.mediator.bus_event import BusEvent


class _EventBus(Mediator):
    def __init__(self):
        self.user_module = UserModule(mediator=self)
        self.session_module = SessionModule(mediator=self)

    def notify(self, sender: MediatorComponent, event: str, data: List = []) -> None:
        self._log(str(sender), event)

        if event == BusEvent.AUTHENTICATION_STARTED:
            self.user_module.on_authorization_started(data)

        if event == BusEvent.CREDENTIALS_CONFIRMED:
            username = data[0]
            self.session_module.on_credentials_confirmed(username)

        if event == BusEvent.AUTHENTICATION_SUCCESSFUL:
            pass

    @staticmethod
    def _log(sender: str, event: str):
        print('[EventBus] Sender: {}, Event: {}'.format(sender, event), flush=True)


bus = _EventBus()
