from pydantic import BaseModel, Field
from flask import Response, make_response
from sessions.adapters import api_service


class Credentials(BaseModel):
    """Credentials required to create session for the User"""
    username: str = Field(description='Username')
    password: str = Field(description='password')


def login_action(credentials: Credentials) -> Response:
    session = api_service.create_session(
        credentials.username,
        credentials.password,
    )

    response = make_response('', 201)
    response.set_cookie('session_id', session.raw_id())
    return response
