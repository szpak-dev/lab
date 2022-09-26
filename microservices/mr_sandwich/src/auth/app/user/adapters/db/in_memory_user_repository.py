from app.user.domain.models.username import Username
from app.user.domain.ports.user_repository import UserRepository
from app.user.domain.models.role import Role
from app.user.domain.models.user import User
from app.user.domain.models.user_id import UserId

users = {"test_user": "john_doe"}


class InMemoryUserRepository(UserRepository):
    def compare_password(self, user: User, plain_password: str) -> bool:
        return True

    def get_by_username(self, username: Username) -> User:
        return User(
            UserId('uid'),
            username,
            Role('SUPER_ADMIN'),
        )
