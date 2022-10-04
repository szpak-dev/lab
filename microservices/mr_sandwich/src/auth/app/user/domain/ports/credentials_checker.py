from abc import ABC, abstractmethod


class CredentialsChecker(ABC):
    @abstractmethod
    def login(self, username: str, password: str):
        pass
