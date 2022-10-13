from abc import ABC, abstractmethod

from sessions.domain.value_objects import Credentials


class SessionTransceiver(ABC):
    @abstractmethod
    def emit_authentication_started(self, credentials: Credentials):
        pass

    @abstractmethod
    def on_credentials_confirmed(self, username: str):
        pass
