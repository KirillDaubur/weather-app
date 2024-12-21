from abc import ABC, abstractmethod


class BaseDB(ABC):
    @abstractmethod
    async def init_db(self):
        pass

    @abstractmethod
    async def save_log_entry(self, city: str, timestamp: int, resource_address: str):
        pass
