from os import getenv
import jwt
from fastapi import Request

from domain.errors import IdentityNotFound
from domain.value_objects import SessionId


def extract_session_id(request: Request) -> SessionId:
    def from_cookie(req: Request):
        if req.cookies.get('session_id'):
            return req.cookies.get('session_id')

    def from_jwt(req: Request):
        header_value = req.headers.get('Authorization')
        if not header_value:
            raise IdentityNotFound

        bearer, encoded_jwt = header_value.split(' ')
        payload = decode_jwt(encoded_jwt)

        if payload.get('sid'):
            return payload.get('sid')

    if from_cookie(request):
        return SessionId(from_cookie(request))

    if from_jwt(request):
        return SessionId(from_jwt(request))

    raise IdentityNotFound


def encode_jwt(session_id: str, username: str, ttl: int) -> str:
    payload = {'sid': session_id, 'username': username, 'ttl': ttl}
    return jwt.encode(payload, getenv('JWT_SECRET'), algorithm='HS256')


def decode_jwt(encoded_jwt: str) -> dict:
    return jwt.decode(encoded_jwt, getenv('JWT_SECRET'), algorithms=["HS256"])