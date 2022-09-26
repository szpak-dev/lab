from abc import ABC, abstractmethod


class Authenticator(ABC):
    @abstractmethod
    def check_credentials(self, username: str, password: str):
        pass
