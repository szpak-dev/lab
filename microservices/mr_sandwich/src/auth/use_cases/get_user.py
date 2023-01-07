from fastapi import Response
from pydantic import BaseModel


class Role(BaseModel):
    """User Role in the system"""
    name: str


class User(BaseModel):
    """Current User object"""
    id: int
    role: Role


def get_user_action():
    pass
