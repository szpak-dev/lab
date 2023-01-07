from domain.errors import SessionNotFound
from domain.ports.session_repository import SessionRepository
from domain.value_objects import Session, SessionId
from shared.shared import generate_number_base64
from domain.value_objects import Username

sessions_by_id = {}
sessions_by_username = {}


class RedisSessionRepository(SessionRepository):
    def get_by_id(self, session_id: SessionId) -> Session:
        raw_session_id = session_id.value

        if not sessions_by_id.get(raw_session_id):
            raise SessionNotFound

        raw_username = sessions_by_id.get(raw_session_id)
        return Session(raw_session_id, raw_username)

    def create_session(self, username: Username) -> Session:
        session = Session(generate_number_base64(40), username.value)
        sessions_by_id[session.id] = session.username
        sessions_by_username[session.username] = session.id

        return session

    def destroy_session(self, session_id: SessionId) -> None:
        raw_username = sessions_by_id.pop(session_id.value)
        sessions_by_username.pop(raw_username)
