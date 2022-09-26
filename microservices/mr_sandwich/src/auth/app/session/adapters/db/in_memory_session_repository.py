from app.session.domain.models.session import Session
from app.session.domain.models.session_id import SessionId
from app.session.domain.ports.session_repository import SessionRepository
from app.user.domain.models.user_id import UserId

active_sessions = {}


class InMemorySessionRepository(SessionRepository):
    def save(self, user_id: UserId) -> SessionId:
        session_id = SessionId.generate()
        active_sessions[user_id] = session_id.id
        return session_id

    def exists(self, session_id: SessionId) -> bool:
        pass

    def remove(self, session_id) -> None:
        pass

    def get(self, session_id) -> Session:
        return Session()
