from abc import ABC, abstractmethod


class JwtRepository(ABC):
    @abstractmethod
    def create(self, username: str) -> None:
        pass

    @abstractmethod
    def assert_is_ours(self, jwt: str) -> bool:
        pass
