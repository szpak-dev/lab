from abc import ABC, abstractmethod
from app.session.domain.models.session import Session
from app.session.domain.models.session_id import SessionId


class SessionRepository(ABC):
    @abstractmethod
    def save(self, user_id: str) -> SessionId:
        pass

    @abstractmethod
    def exists(self, session_id: SessionId) -> bool:
        pass

    @abstractmethod
    def remove(self, session_id) -> None:
        pass

    @abstractmethod
    def get(self, session_id) -> Session:
        pass
