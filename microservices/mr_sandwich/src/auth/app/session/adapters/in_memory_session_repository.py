from session.domain.errors import SessionNotFound
from session.domain.value_objects import SessionId, Session
from app.session.domain.ports.session_repository import SessionRepository

active_sessions = {}


class InMemorySessionRepository(SessionRepository):
    def save(self, user_id: str) -> SessionId:
        session_id = SessionId.generate()
        active_sessions[user_id] = session_id.id
        return session_id

    def exists(self, session_id: str) -> bool:
        pass

    def remove(self, session_id: str) -> None:
        pass

    def get(self, session_id: str) -> Session:
        return Session('session-id')

    def get_for_user(self, user_id: str) -> Session:
        session_id = active_sessions.get(user_id)
        if session_id:
            return Session(session_id)

        raise SessionNotFound
