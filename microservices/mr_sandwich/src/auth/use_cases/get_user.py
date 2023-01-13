from fastapi import Request, HTTPException
from pydantic import BaseModel

from adapters import user_repository, session_repository
from domain.errors import IdentityNotFound, SessionNotFound, UserNotFound
from domain.services import extract_session_id


class User(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True


async def get_user_action(request: Request) -> User:
    try:
        session_id = extract_session_id(request)
        session = session_repository.get_by_id(session_id)

        return await user_repository.get_by_id(session.user_id)
    except (IdentityNotFound, SessionNotFound, UserNotFound) as e:
        raise HTTPException(status_code=401, detail=str(e))
