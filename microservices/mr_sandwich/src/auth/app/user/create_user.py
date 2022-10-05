from app.user.adapters import user_repository
from app.user.domain.entities.user import user_factory
from app.user.domain.errors import UserAlreadyExists
from app.ddd.application import ApplicationCommand
from app.user.domain.value_objects import PlainPassword, Username


class CreateUser(ApplicationCommand):
    def __init__(self, username: str, plain_password: str):
        user = user_repository.get_by_username(username)
        if user:
            raise UserAlreadyExists

        user = user_factory(Username(username), PlainPassword(plain_password))
        user_repository.save(user)
