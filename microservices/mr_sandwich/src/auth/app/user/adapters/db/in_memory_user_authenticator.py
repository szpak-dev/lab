from app.session.adapters.db.in_memory_session_repository import InMemorySessionRepository
from app.user.domain.ports.authenticator import Authenticator
from app.user.adapters.db.in_memory_user_repository import InMemoryUserRepository
from app.user.domain.models.username import Username

session_repository = InMemorySessionRepository()
user_repository = InMemoryUserRepository()


class InMemoryUserAuthenticator(Authenticator):
    def check_credentials(self, username: str, plain_password: str):
        user = user_repository.get_by_username(Username(username))

        if user and user_repository.compare_password(user, plain_password):
            return session_repository.save(user.id)

        return False
