from fastapi import Request, HTTPException
from pydantic import BaseModel

from adapters import user_repository, session_repository
from domain.errors import IdentityNotFound, SessionNotFound, UserNotFound
from domain.services import extract_session_id
from domain.value_objects import Username


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


def get_user_action(request: Request):
    try:
        session_id = extract_session_id(request)
        session = session_repository.get_by_id(session_id)

        username = Username(session.username)
        return user_repository.get_by_username(username)
    except (IdentityNotFound, SessionNotFound, UserNotFound):
        raise HTTPException(status_code=401, detail='No valid Session')
