from typing import List

from logger import logging
from mediator import Mediator, MediatorComponent
from mediator.bus_event import BusEvent
from sessions.domain.ports.session_transceiver import SessionTransceiver
from users.domain.ports.user_transceiver import UserTransceiver


class _EventBus(Mediator):
    session_transceiver: SessionTransceiver = None
    user_transceiver: UserTransceiver = None

    def notify(self, sender: MediatorComponent, event: str, data: List = []) -> None:
        logging.info('[EventBus] {}'.format(event))

        if event == BusEvent.AUTHENTICATION_STARTED:
            self.user_transceiver.on_authentication_started(data)

        if event == BusEvent.CREDENTIALS_CONFIRMED:
            username = data[0]
            self.session_transceiver.on_credentials_confirmed(username)

        if event == BusEvent.AUTHENTICATION_SUCCESSFUL:
            pass


event_bus = _EventBus()
