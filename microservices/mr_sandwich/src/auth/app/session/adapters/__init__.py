from app.session.domain.ports.session_repository import SessionRepository
from app.session.domain.ports.jwt_repository import JwtRepository
from app.session.adapters.in_memory_session_repository import InMemorySessionRepository
from app.session.adapters.in_memory_jwt_repository import InMemoryJwtRepository

session_repository: SessionRepository = InMemorySessionRepository()
jwt_repository: JwtRepository = InMemoryJwtRepository()
