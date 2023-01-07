from abc import ABC, abstractmethod

from domain.value_objects import Username, SessionId, Session


class SessionRepository(ABC):
    @abstractmethod
    def create_session(self, username: Username) -> Session:
        pass

    @abstractmethod
    def destroy_session(self, session_id: SessionId) -> None:
        pass

    @abstractmethod
    def get_by_id(self, session_id: SessionId) -> Session:
        pass
