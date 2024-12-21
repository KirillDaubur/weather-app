from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from services.db import BaseDB
from services.db.sql_db.models import LogEntry, Base
from settings import Settings, get_settings


class SqlDb(BaseDB):
    def __init__(self, settings: Settings = get_settings()):
        self.engine: AsyncEngine = create_async_engine(settings.postgres_url, echo=True, future=True)
        self.async_session = async_sessionmaker(bind=self.engine, class_=AsyncSession, expire_on_commit=False)

    async def init_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def get_session(self):
        session = self.async_session()

        try:
            yield session
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()

    async def save_log_entry(self, city: str, timestamp: int, resource_address: str):
        """
        Save a log entry into the database.
        """
        # async with self.get_session() as session:
        #     log_entry = LogEntry(city_name=city, timestamp=datetime.now(), resource_address=resource_address)
        #     session.add(log_entry)
        #     await session.commit()
        #     await session.refresh(log_entry)
        #     print(f"LogEntry saved: {log_entry}")
        #     return log_entry

        async with AsyncSession(self.engine) as session:
            log_entry = LogEntry(city_name=city, timestamp=datetime.now(), resource_address=resource_address)
            session.add(log_entry)
            await session.commit()
            await session.refresh(log_entry)
            return log_entry