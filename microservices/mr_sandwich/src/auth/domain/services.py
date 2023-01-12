from os import getenv
import jwt
from fastapi import Request

from domain.auth import JwtClaims
from domain.errors import IdentityNotFound
from domain.value_objects import SessionId


def extract_session_id(request: Request) -> SessionId:
    def from_cookie(req: Request):
        if req.cookies.get('session_id'):
            return req.cookies.get('session_id')

    def from_header(req: Request):
        header_value = req.headers.get('Authorization')
        if not header_value:
            raise IdentityNotFound

        return req.headers.get('Authorization' )

    if from_cookie(request):
        return SessionId(from_cookie(request))

    if from_header(request):
        return SessionId(from_header(request))

    raise IdentityNotFound


def encode_jwt(jwt_claims: JwtClaims) -> str:
    return jwt.encode(jwt_claims, getenv('JWT_SECRET'), algorithm='HS256')


def decode_jwt(encoded_jwt: str) -> dict:
    return jwt.decode(encoded_jwt, getenv('JWT_SECRET'), algorithms=["HS256"])
