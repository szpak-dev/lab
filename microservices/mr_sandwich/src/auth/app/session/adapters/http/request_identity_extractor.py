from flask import Request

from app.session.domain.models.identity import Identity
from app.session.domain.models.jwt import Jwt
from app.session.domain.models.session_id import SessionId
from app.session.domain.ports.identity_extractor import IdentityExtractor


class RequestIdentityExtractor(IdentityExtractor):
    def extract(self, request: Request) -> Identity:
        session_id = self._extract_session_id(request)
        if session_id:
            return Identity(session_id=SessionId(session_id))

        jwt = self._extract_jwt(request)
        if jwt:
            return Identity(jwt=Jwt(jwt))

        raise RuntimeError('No Identity found within Request')

    @staticmethod
    def _extract_session_id(flask_request: Request):
        if flask_request.cookies.get('session_id'):
            return flask_request.cookies.get('session_id')
        return False

    @staticmethod
    def _extract_jwt(flask_request: Request):
        if flask_request.headers.get('Authorization'):
            return flask_request.headers.get('Authorization')
        return False


