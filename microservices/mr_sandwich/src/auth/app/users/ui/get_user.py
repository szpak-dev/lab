from pydantic import BaseModel, Field
from flask import Response, make_response
from users.adapters import api_service


class Role(BaseModel):
    """User Role in the system"""
    name: str = Field(description='Name of the Role')


class User(BaseModel):
    """Current User object"""
    id: int = Field(description='User Id')
    role: Role = Field(description='User Role')


def get_user_action(username: str) -> Response:
    user = api_service.get_user(username)
    return make_response(user.serialize(), 200)
