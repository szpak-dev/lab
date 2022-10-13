from abc import ABC, abstractmethod


class CredentialsChecker(ABC):
    @abstractmethod
    def check(self, username: str, password: str):
        pass
