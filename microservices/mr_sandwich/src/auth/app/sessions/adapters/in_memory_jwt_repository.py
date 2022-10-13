from sessions.domain.ports.jwt_repository import JwtRepository
from sessions.domain.errors import SessionNotFound


class InMemoryJwtRepository(JwtRepository):
    def create(self, username: str) -> None:
        pass

    def assert_is_ours(self, jwt: str) -> None:
        if len(jwt) < 2:
            raise SessionNotFound('JWT found in header does not exist')
