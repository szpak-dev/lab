from domain.entities import User, UserRole
from domain.errors import UserNotFound, UserAlreadyExists
from domain.ports.user_repository import UserRepository
from domain.value_objects import Username, PlainPassword
from shared.db import db_session


class SqlUserRepository(UserRepository):
    def get_by_username(self, username: Username) -> User:
        user = db_session.query(User).filter(
            User.username == username.value
        ).join(UserRole, isouter=True).first()

        if not user:
            raise UserNotFound

        return user

    def add_new(self, username: Username, plain_password: PlainPassword) -> None:
        try:
            self.get_by_username(username)
            raise UserAlreadyExists
        except UserNotFound:
            user = User()
            user.username = username.value
            user.password = plain_password.encode().encoded
            self.save(user)

    def save(self, user: User) -> None:
        with db_session as session:
            session.add(user)
            session.commit()
