from abc import ABC, abstractmethod

from app.ddd.repository import BaseRepository
from app.session.domain.value_objects import Session


class SessionRepository(BaseRepository):
    @abstractmethod
    def save(self, username: str) -> None:
        pass

    @abstractmethod
    def exists(self, session_id: str) -> bool:
        pass

    @abstractmethod
    def assert_exists(self, session_id: str) -> None:
        pass

    @abstractmethod
    def remove(self, session_id: str) -> None:
        pass

    @abstractmethod
    def get(self, session_id: str) -> Session:
        pass

    @abstractmethod
    def get_for_user(self, username: str) -> Session:
        pass
