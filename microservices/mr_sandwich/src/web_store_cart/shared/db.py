from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_DSN = getenv('DATABASE_DSN', 'postgresql://postgres:postgres@localhost:5435/web_store_cart')
engine = create_engine(DATABASE_DSN)

DbSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

db_session = DbSession()

Base = declarative_base()
