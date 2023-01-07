from adapters.redis_session_repository import RedisSessionRepository
from adapters.sql_user_repository import SqlUserRepository
from domain.ports.session_repository import SessionRepository
from domain.ports.user_repository import UserRepository

user_repository: UserRepository = SqlUserRepository()
session_repository: SessionRepository = RedisSessionRepository()