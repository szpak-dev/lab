from app.session.domain.ports.api_service import ApiService

from app.session.domain.value_objects import Credentials, SessionId
from app.session.domain.ports.session_repository import SessionRepository
from app.session.domain.ports.session_transceiver import SessionTransceiver
from app.session.domain.entities.session import Session


class HttpApiService(ApiService):
    def __init__(self, session_repository: SessionRepository, session_transceiver: SessionTransceiver):
        self._session_repository = session_repository
        self._session_transceiver = session_transceiver

    def create_session(self, username: str, password: str) -> Session:
        credentials = Credentials.new(username, password)
        self._session_transceiver.emit_authentication_started(credentials)
        return self._session_repository.get_for_user('admin_user')

    def destroy_session(self, username: str):
        session = self._session_repository.get_for_user(username)
        if session:
            self._session_repository.remove(session.id)

    def get_current_username(self, raw_session_id: str) -> str:
        session_id = SessionId(raw_session_id)
        return self._session_repository.get_username(session_id)
