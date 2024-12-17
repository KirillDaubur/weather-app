from services.weather_service.openweathermap.openweathermap_wrapper import OpenWeatherMapWrapper
from services.weather_service.base_weather_service import BaseWeatherService


class WeatherServiceSingleton:
    _instance: BaseWeatherService = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = OpenWeatherMapWrapper()

        return cls._instance

def get_weather_service():
    return WeatherServiceSingleton.get_instance()