from abc import ABC, abstractmethod

from services.db.models import LogEntry


class BaseDB(ABC):
    @abstractmethod
    async def save_log_entry(self, city: str, timestamp: int, resource_address: str):
        pass
