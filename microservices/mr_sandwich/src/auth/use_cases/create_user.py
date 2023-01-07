from pydantic import BaseModel
from fastapi import HTTPException

from adapters import user_repository
from domain.errors import UserAlreadyExists
from domain.value_objects import Username, PlainPassword


class Registration(BaseModel):
    username: str
    password: str
    repeat_password: str

    def username(self) -> Username:
        return Username(self.username)

    def password(self) -> PlainPassword:
        return PlainPassword(self.password)


def create_user_action(registration: Registration) -> None:
    try:
        user_repository.add_new(
            registration.username(),
            registration.password(),
        )
    except UserAlreadyExists as e:
        raise HTTPException(status_code=400, detail=str(e))
