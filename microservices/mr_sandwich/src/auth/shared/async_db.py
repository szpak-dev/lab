import asyncio
import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_ASYNC_DSN = os.getenv('DATABASE_ASYNC_DSN', 'postgresql+asyncpg://postgres:postgres@localhost:5433/auth')
engine = create_async_engine(DATABASE_ASYNC_DSN)

async_session = sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)

Base = declarative_base()
