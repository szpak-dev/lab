from domain.ports.session_repository import SessionRepository
from domain.value_objects import Session
from shared.shared import generate_number_base64
from domain.value_objects import Username


class RedisSessionRepository(SessionRepository):
    def create_session(self, username: Username):
        session = Session(
            generate_number_base64(40),
            username.value,
        )

    def destroy_session(self, username: str):
        pass

    def get_current_username(self, raw_session_id: str):
        pass

