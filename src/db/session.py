"""Модуль по работе с асинхронным БД-интерфейсом"""
from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
)
from sqlalchemy.orm import sessionmaker

from src.config.configs import get_settings


class AsyncDb:
    """Класс для работы с асинхронным БД-интерфейсом"""

    def __init__(self, db_settings: dict[str, Any]):
        self._engine: AsyncEngine = create_async_engine(**db_settings)

    def create_session_maker(self):
        """
        Возвращает класс сессии БД-интерфейса
        """
        return sessionmaker(self._engine, future=True, expire_on_commit=False, class_=AsyncSession)

    async def close(self):
        """
        Закрывает БД-интерфейс
        """
        await self._engine.dispose()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session



settings = get_settings()

db_engine = AsyncDb(settings.database)
db_session_maker = db_engine.create_session_maker()

engine = create_async_engine(**settings.database)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


