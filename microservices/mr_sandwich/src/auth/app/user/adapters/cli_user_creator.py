from app.user.domain.ports.user_creator import UserCreator
from app.user.domain.entities.user import user_factory
from app.user.domain.errors import UserAlreadyExists
from app.user.domain.value_objects import PlainPassword, Username
from app.user.domain.ports.user_repository import UserRepository


class CliUserCreator(UserCreator):
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def create(self, username: str, password: str):
        user = self._user_repository.get_by_username(username)
        if user:
            raise UserAlreadyExists

        user = user_factory(Username(username), PlainPassword(password))
        self._user_repository.save(user)
