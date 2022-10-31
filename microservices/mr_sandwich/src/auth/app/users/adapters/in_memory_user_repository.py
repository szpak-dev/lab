from users.domain.entities.user import User
from users.domain.ports.user_repository import UserRepository
from users.domain.errors import UserNotFound
from users.domain.value_objects import UserId, Username, Password, Role

users = {
    "admin_user": "password",
    "chef_user": "password",
    "customer_user": "password",
    "deliverer_user": "password",
}


class InMemoryUserRepository(UserRepository):
    def get_by_username(self, username: str) -> User:
        if not users.get(username):
            raise UserNotFound

        return User(
            UserId('id'),
            Username(username),
            Password('password'),
            Role('r')
        )

    def save(self, user: User) -> None:
        pass