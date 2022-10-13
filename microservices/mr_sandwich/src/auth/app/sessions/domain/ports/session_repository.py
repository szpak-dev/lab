from abc import abstractmethod

from shared import BaseRepository
from sessions.domain.value_objects import SessionId
from sessions.domain.entities.session import Session


class SessionRepository(BaseRepository):
    @abstractmethod
    def save(self, username: str) -> None:
        pass

    @abstractmethod
    def exists(self, session_id: SessionId) -> bool:
        pass

    @abstractmethod
    def assert_exists(self, session_id: SessionId) -> None:
        pass

    @abstractmethod
    def remove(self, session_id: SessionId) -> None:
        pass

    @abstractmethod
    def get(self, session_id: SessionId) -> Session:
        pass

    @abstractmethod
    def get_for_user(self, username: str) -> Session:
        pass

    @abstractmethod
    def get_username(self, session_id: SessionId) -> str:
        pass
