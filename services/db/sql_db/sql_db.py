from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import SQLModel, create_engine

from services.db.base_db import BaseDB
from services.db.models import LogEntry
from settings import Settings, get_settings


class SqlDb(BaseDB):
    def __init__(self, settings: Settings = Depends(get_settings)):
        """
        Initialize the database connection.
        """
        self.engine = AsyncEngine(create_engine(settings.database_url, echo=True, future=True))

    async def init_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(SQLModel.metadata.create_all)

    async def get_session(self) -> AsyncSession:
        async_session = async_sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

        async with async_session() as session:
            yield session

    async def save_log_entry(self, city: str, timestamp: int, resource_address: str):
        """
        Save a log entry to the database.
        """
        async with self.get_session() as session:
            log_entry = LogEntry(city=city, timestamp=timestamp, resource_address=resource_address)
            session.add(log_entry)
            await session.commit()
            await session.refresh(log_entry)
            print(f"LogEntry saved: {log_entry}")
            return log_entry
