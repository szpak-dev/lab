from app.user.domain.ports.user_repository import UserRepository
from app.user.domain.entities.user import User, create_user

users = {"test_user": "john_doe"}


class InMemoryUserRepository(UserRepository):
    def get_by_username(self, username: str) -> User:
        return create_user()

    def save(self, user: User) -> None:
        pass
    