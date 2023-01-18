import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DEFAULT_DSN = 'postgresql+asyncpg://postgres:postgres@localhost:5435/web_store_cart'
DATABASE_ASYNC_DSN = os.getenv('DATABASE_ASYNC_DSN', DEFAULT_DSN)

engine = create_async_engine(DATABASE_ASYNC_DSN)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()
