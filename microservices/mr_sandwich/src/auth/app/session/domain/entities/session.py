from dataclasses import dataclass
from typing import TypeVar

from app.session.domain.value_objects import SessionId

S = TypeVar('S', bound='Session')


@dataclass()
class Session:
    def __init__(self, session_id: SessionId = None):
        if session_id is None:
            session_id = SessionId.new()
        self._id = session_id

    @property
    def id(self):
        return self._id

    @classmethod
    def new(cls) -> S:
        return Session()

    def raw_id(self) -> str:
        return str(self._id.raw())
