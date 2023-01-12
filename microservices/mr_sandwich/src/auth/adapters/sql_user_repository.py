from domain.entities import User, UserRole
from domain.errors import UserNotFound
from domain.ports.user_repository import UserRepository
from domain.value_objects import Username, UserId
from shared.db import db_session


class SqlUserRepository(UserRepository):
    def get_by_id(self, user_id: UserId) -> User:
        user = db_session.query(User).filter(
            User.id == user_id.id
        ).join(UserRole, isouter=True).first()

        if not user:
            raise UserNotFound

        return user

    def get_by_username(self, username: Username) -> User:
        user = db_session.query(User).filter(
            User.username == username.value
        ).join(UserRole, isouter=True).first()

        if not user:
            raise UserNotFound

        return user

    def save(self, user: User) -> None:
        with db_session as session:
            session.add(user)
            session.commit()
