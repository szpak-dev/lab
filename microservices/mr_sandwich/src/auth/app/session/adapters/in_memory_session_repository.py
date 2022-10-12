from app.session.domain.errors import SessionNotFound
from app.session.domain.value_objects import SessionId
from app.session.domain.ports.session_repository import SessionRepository
from app.session.domain.entities.session import Session

active_sessions = {}
active_sessions_by_username = {}


class InMemorySessionRepository(SessionRepository):
    def save(self, username: str) -> None:
        session = Session.new()
        raw_session_id = session.raw_id()

        active_sessions[raw_session_id] = username
        active_sessions_by_username[username] = raw_session_id

    def exists(self, session_id: SessionId) -> bool:
        return bool(active_sessions.get(session_id.raw()))

    def assert_exists(self, session_id: SessionId) -> None:
        if not self.exists(session_id):
            raise SessionNotFound('Session Id found in cookie does not exist')

    def remove(self, session_id: SessionId) -> None:
        pass

    def get(self, session_id: SessionId) -> Session:
        return Session(session_id)

    def get_for_user(self, username: str) -> Session:
        raw_session_id = active_sessions_by_username.get(username)
        if not raw_session_id:
            raise SessionNotFound

        return Session(SessionId(raw_session_id))

    def get_username(self, session_id: SessionId) -> str:
        username = active_sessions.get(session_id.raw())
        if not username:
            raise SessionNotFound

        return username
