from flask import Request
from requests import Response

from app.session.adapters import session_repository
from app.session.adapters.http.request_identity_extractor import HttpRequestIdentityExtractor
from app.session.adapters.http.request_passer import HttpRequestPasser
from app.session.adapters.http.jwt_manager import JwtManager
from app.session.domain.value_objects import Identity
from app.session.domain.errors import SessionNotFound
from app.session.adapters.http.passable_request_factory import PassableRequestFactory


def extract_identity(flask_request: Request):
    return HttpRequestIdentityExtractor().extract(flask_request)


def confirm_session(identity: Identity) -> None:
    if identity.requested_from_internet():
        if not session_repository().get(identity.value()):
            raise SessionNotFound('Session Id found in cookie does not exist')
    elif identity.requested_from_subnet():
        if not JwtManager().validate(identity.value()):
            raise SessionNotFound('JWT found in header does not exist')
    else:
        raise SessionNotFound


def create_passable_request(identity: Identity, flask_request: Request):
    if identity.requested_from_internet():
        return PassableRequestFactory().create_internet_request(flask_request)
    elif identity.requested_from_subnet():
        return PassableRequestFactory().create_subnet_request(flask_request)


def pass_request(flask_request: Request) -> Response:
    return HttpRequestPasser().execute(flask_request)
