from abc import ABC, abstractmethod


class BaseCache(ABC):
    @abstractmethod
    async def get_city_cache(self, city: str):
        pass

    @abstractmethod
    async def set_city_cache(self, city: str, value: str):
        pass