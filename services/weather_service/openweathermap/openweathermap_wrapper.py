import ssl
from typing import List, Dict

import aiohttp

from errors import IncorrectCityNameError, WeatherAPIError
from services.weather_service.base_weather_service import BaseWeatherService
from settings import Settings, get_settings


class OpenWeatherMapWrapper(BaseWeatherService):

    def __init__(self, settings: Settings = get_settings()):
        self.api_key = settings.openweathermap_app_id

    async def get_weather(self, city: str) -> dict:
        coords = await self._get_city_coords(city)
        return await self._get_weather_data_by_city_coords(coords)


    async def _get_city_coords(self, city: str) -> dict:
        url = "https://api.openweathermap.org/geo/1.0/direct"
        params = {
            "q": city,
            "appid": self.api_key,
            "limit": 1
        }

        response: List[Dict] = await self._get_json_response(url, params)

        if not response:
            raise IncorrectCityNameError

        return {
            "lat": response[0].get("lat"),
            "lon": response[0].get("lon")
        }

    async def _get_weather_data_by_city_coords(self, coords: Dict) -> Dict:
        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            **coords,
            "appid": self.api_key,
        }

        return await self._get_json_response(url, params)

    async def _get_json_response(self, url, params):
        # Custom SSL context to bypass certificate validation
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params, ssl=ssl_context) as response:
                if response.status == 200:
                    return await response.json()

                raise WeatherAPIError(f"Failed to fetch data. HTTP Status: {response.status}")
