from contextlib import asynccontextmanager
from functools import cache
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from app.core.settings import get_settings

settings = get_settings()


@cache
def get_async_engine():
    return create_async_engine(
        "postgresql+asyncpg://" + settings.get_postgres_url,
        pool_size=3,
        max_overflow=5,
        future=True,
        echo=False,
    )


@cache
def get_general_session_maker() -> async_sessionmaker[AsyncSession]:
    engine = get_async_engine()
    return async_sessionmaker(
        bind=engine,
        autoflush=False,
        expire_on_commit=False,  # Prevent object expiration after commit
    )


async def get_general_session() -> AsyncGenerator[AsyncSession, None]:
    session_maker = get_general_session_maker()
    async with session_maker() as session:
        try:
            yield session
        finally:
            await session.close()


@asynccontextmanager
async def get_session_without_depends() -> AsyncGenerator[AsyncSession, None]:
    engine = get_async_engine()
    session_maker = async_sessionmaker(
        bind=engine, autoflush=False, autocommit=False, expire_on_commit=False
    )
    async with session_maker() as session:
        try:
            yield session
        finally:
            await session.close()
