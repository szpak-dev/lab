from abc import abstractmethod

from shared import BaseRepository


class JwtRepository(BaseRepository):
    @abstractmethod
    def create(self, username: str) -> None:
        pass

    @abstractmethod
    def assert_is_ours(self, jwt: str) -> bool:
        pass
