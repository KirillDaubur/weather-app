from abc import ABC, abstractmethod


class BaseWeatherService(ABC):
    @abstractmethod
    async def get_weather(self, city: str) -> dict:
        pass