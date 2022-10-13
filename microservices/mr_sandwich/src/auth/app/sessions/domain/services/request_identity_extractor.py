from flask import Request as FlaskRequest

from sessions.domain.value_objects import Identity, SessionId, Jwt
from sessions.domain.errors import IdentityNotFound


class _HttpRequestIdentityExtractor:
    def extract(self, flask_request: FlaskRequest) -> Identity:
        session_id = self._extract_session_id(flask_request)
        if session_id:
            return Identity(session_id=SessionId(session_id))

        jwt = self._extract_jwt(flask_request)
        if jwt:
            return Identity(jwt=Jwt(jwt))

        raise IdentityNotFound

    @staticmethod
    def _extract_session_id(flask_request: FlaskRequest):
        if flask_request.cookies.get('session_id'):
            return flask_request.cookies.get('session_id')

        return False

    @staticmethod
    def _extract_jwt(flask_request: FlaskRequest):
        if flask_request.headers.get('Authorization'):
            return flask_request.headers.get('Authorization')

        return False


def extract_identity(flask_request: FlaskRequest) -> Identity:
    return _HttpRequestIdentityExtractor().extract(flask_request)
