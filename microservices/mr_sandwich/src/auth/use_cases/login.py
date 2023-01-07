from pydantic import BaseModel
from fastapi import Response, HTTPException

from adapters import user_repository, session_repository
from domain.errors import UserError, PasswordDoesNotMatch
from domain.value_objects import Username, PlainPassword


class Credentials(BaseModel):
    username: str
    password: str

    @classmethod
    def split(cls, credentials):
        return Username(credentials.username), PlainPassword(credentials.password)


def login_action(credentials: Credentials, response: Response):
    try:
        username, password = Credentials.split(credentials)

        user = user_repository.get_by_username(username)
        user.check_password(password)

        session = session_repository.create_session(username)
        response.set_cookie('session_id', session.id)
    except (UserError, PasswordDoesNotMatch):
        raise HTTPException(status_code=401, detail='Invalid credentials')
