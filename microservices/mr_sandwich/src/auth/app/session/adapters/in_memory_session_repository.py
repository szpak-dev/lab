from app.session.domain.errors import SessionNotFound
from app.session.domain.value_objects import SessionId, Session
from app.session.domain.ports.session_repository import SessionRepository

active_sessions = {}
active_sessions_by_username = {}


class InMemorySessionRepository(SessionRepository):
    def with_type(self):
        return self

    def save(self, username: str) -> None:
        session_id = SessionId.generate()

        active_sessions[session_id.id] = username
        active_sessions_by_username[username] = session_id.id

    def exists(self, session_id: str) -> bool:
        return bool(active_sessions.get(session_id))

    def assert_exists(self, session_id: str) -> None:
        if not self.exists(session_id):
            raise SessionNotFound('Session Id found in cookie does not exist')

    def remove(self, session_id: str) -> None:
        pass

    def get(self, session_id: str) -> Session:
        return Session('sid')

    def get_for_user(self, username: str) -> Session:
        # session_id = active_sessions.get(username)
        # if not session_id:
        #     raise SessionNotFound

        session_id = 'sid'
        return Session(session_id)


