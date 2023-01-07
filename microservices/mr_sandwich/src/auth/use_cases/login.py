from pydantic import BaseModel
from fastapi import Response, HTTPException

from domain.errors import UserError
from domain.value_objects import Username, PlainPassword


class Credentials(BaseModel):
    username: str
    password: str

    def username(self) -> Username:
        return Username(self.username)

    def password(self) -> PlainPassword:
        return PlainPassword(self.password)


def login_action(credentials: Credentials, response: Response):
    try:

    except UserError:
        raise HTTPException(status_code=401, detail='Invalid credentials')