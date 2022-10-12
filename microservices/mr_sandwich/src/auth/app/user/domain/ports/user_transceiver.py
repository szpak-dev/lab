from abc import ABC, abstractmethod


class UserTransceiver(ABC):
    @abstractmethod
    def on_authentication_started(self, data):
        pass

    @abstractmethod
    def emit_credentials_confirmed(self, username: str):
        pass
