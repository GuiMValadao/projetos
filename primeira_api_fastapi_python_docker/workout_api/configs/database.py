<<<<<<< HEAD
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from workout_api.configs.settings import settings

engine = create_async_engine(settings.DB_URL, echo=False)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session
=======
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from workout_api.configs.settings import settings

engine = create_async_engine(settings.DB_URL, echo=False)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_session() -> AsyncGenerator:
    async with async_session() as session:
        yield session
>>>>>>> 9e50be3a49701ce9c08b289a60135d291fc6a2fe
