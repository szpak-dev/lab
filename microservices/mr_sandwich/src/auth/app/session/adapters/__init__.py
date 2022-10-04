from app.session.domain.ports.session_repository import SessionRepository
from app.session.domain.ports.jwt_repository import JwtRepository

from app.session.adapters.in_memory_session_repository import InMemorySessionRepository
from app.session.adapters.in_memory_jwt_repository import InMemoryJwtRepository


def session_repository() -> SessionRepository:
    return InMemorySessionRepository()


def jwt_repository() -> JwtRepository:
    return InMemoryJwtRepository()