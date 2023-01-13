from pydantic import BaseModel
from fastapi import HTTPException

from adapters import user_repository
from domain.entities import User
from domain.errors import UserAlreadyExists, UserNotFound
from domain.value_objects import Username, PlainPassword


class Registration(BaseModel):
    username: str
    password: str
    repeat_password: str

    @classmethod
    def split(cls, registration):
        return Username(registration.username), PlainPassword(registration.password)


async def create_user_action(registration: Registration) -> None:
    username, password = Registration.split(registration)

    try:
        await user_repository.get_by_username(username)
        raise UserAlreadyExists
    except UserAlreadyExists as e:
        raise HTTPException(status_code=400, detail=str(e))
    except UserNotFound:
        user = User()
        user.username = username.value
        user.password = password.encode().encoded
        user_repository.save(user)
