from app.user.adapters import user_repository
from app.user.domain.entities.user import create_user
from app.user.domain.errors import UserAlreadyExists


class CreateUser:
    def run(self, username: str, plain_password: str):
        user = user_repository().get_by_username(username)
        if user:
            raise UserAlreadyExists

        user = create_user()
        user_repository().save(user)

        return user