from app.session.domain.errors import SessionNotFound
from app.session.domain.value_objects import SessionId, Session
from app.session.domain.ports.session_repository import SessionRepository

active_sessions = {}
active_sessions_by_user_id = {}


class InMemorySessionRepository(SessionRepository):
    def save(self, user_id: str) -> None:
        session_id = SessionId.generate()
        active_sessions[session_id.id] = user_id
        active_sessions_by_user_id[user_id] = session_id.id

    def exists(self, session_id: str) -> bool:
        return bool(active_sessions.get(session_id))

    def assert_exists(self, session_id: str) -> None:
        if not self.exists(session_id):
            raise SessionNotFound('Session Id found in cookie does not exist')

    def remove(self, session_id: str) -> None:
        pass

    def get(self, session_id: str) -> Session:
        return Session('session-id')

    def get_for_user(self, username: str) -> Session:
        session_id = active_sessions.get(username)
        if session_id:
            return Session(session_id)

        raise SessionNotFound
