from domain.entities import User, UserRole
from domain.errors import UserNotFound
from domain.ports.user_repository import UserRepository
from domain.value_objects import Username, UserId
from shared.async_db import async_session
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound


class SqlUserRepository(UserRepository):
    async def get_by_id(self, user_id: UserId) -> User:
        user_id = int(user_id.id)
        async with async_session() as session:
            try:
                result = await session.execute(
                    select(User)
                    .filter(User.id == user_id)
                    .join(UserRole, isouter=True)
                )

                return result.scalars().one()
            except NoResultFound:
                raise UserNotFound

    async def get_by_username(self, username: Username) -> User:
        username = username.value
        async with async_session() as session:
            try:
                result = await session.execute(
                    select(User)
                    .filter(User.username == username)
                    .join(UserRole, isouter=True)
                )

                return result.scalars().one()
            except NoResultFound:
                raise UserNotFound

    async def save(self, user: User) -> None:
        async with async_session as session:
            session.add(user)
            session.commit()
