from abc import ABC, abstractmethod


class BaseStorage(ABC):
    @abstractmethod
    async def store(self, filename: str, data: dict) -> None:
        pass

    @abstractmethod
    async def load(self, filename: str) -> dict:
        pass