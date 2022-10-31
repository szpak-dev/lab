from flask import Request as FlaskRequest
from requests import Response

from sessions.domain.services.request_identity_extractor import extract_identity
from sessions.domain.services.passable_request_factory import create_passable_request
from sessions.domain.services.request_passer import pass_request
from sessions.domain.ports.request_interceptor import RequestInterceptor
from sessions.domain.ports.session_repository import SessionRepository
from sessions.domain.ports.jwt_repository import JwtRepository
from sessions.domain.value_objects import Identity, SessionId
from sessions.domain.errors import SessionNotFound


class HttpRequestInterceptor(RequestInterceptor):
    def __init__(self, session_repository: SessionRepository, jwt_repository: JwtRepository):
        self._session_repository = session_repository
        self._jwt_repository = jwt_repository

    def pass_request(self, flask_request: FlaskRequest) -> Response:
        identity = extract_identity(flask_request)
        self._assert_valid_identity(identity)

        passable_request = create_passable_request(identity, flask_request)
        response = pass_request(passable_request)

        return response

    def _assert_valid_identity(self, identity: Identity):
        value = identity.value()

        if identity.requested_from_internet():
            session_id = SessionId(value)
            return self._session_repository.assert_exists(session_id)

        if identity.requested_from_subnet():
            return self._jwt_repository.assert_is_ours(value)

        raise SessionNotFound