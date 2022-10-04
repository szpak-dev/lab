from abc import ABC, abstractmethod
from session.domain.value_objects import SessionId, Session


class SessionRepository(ABC):
    @abstractmethod
    def save(self, user_id: str) -> SessionId:
        pass

    @abstractmethod
    def exists(self, session_id: str) -> bool:
        pass

    @abstractmethod
    def remove(self, session_id: str) -> None:
        pass

    @abstractmethod
    def get(self, session_id: str) -> Session:
        pass

    @abstractmethod
    def get_for_user(self, user_id: str) -> Session:
        pass
