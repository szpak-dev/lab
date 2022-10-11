from typing import List

from app.mediator import Mediator, MediatorComponent
from app.mediator.bus_event import BusEvent
from app.session.domain.ports.session_transceiver import SessionTransceiver
from app.user.domain.ports.user_transceiver import UserTransceiver


class _EventBus(Mediator):
    session_transceiver: SessionTransceiver = None
    user_transceiver: UserTransceiver = None

    def notify(self, sender: MediatorComponent, event: str, data: List = []) -> None:
        self._log(sender, event)

        if event == BusEvent.AUTHENTICATION_STARTED:
            self.user_transceiver.on_authorization_started(data)

        if event == BusEvent.CREDENTIALS_CONFIRMED:
            username = data[0]
            self.session_transceiver.on_credentials_confirmed(username)

        if event == BusEvent.AUTHENTICATION_SUCCESSFUL:
            pass

    @staticmethod
    def _log(sender: MediatorComponent, event: str):
        sender_class = sender.__class__.__name__
        print('[EventBus] {}, {}'.format(sender_class, event), flush=True)


event_bus = _EventBus()
