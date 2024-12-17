from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks

from errors import IncorrectCityNameError, WeatherAPIError
from services.cache import BaseCache, get_cache
from services.storage import BaseStorage, get_storage
from services.weather_service import get_weather_service
from services.weather_service.base_weather_service import BaseWeatherService
from utils import get_weather_data_filename

app = FastAPI()


@app.get("/weather")
async def weather(
        background_tasks: BackgroundTasks,
        city: str = "",
        weather_service: BaseWeatherService = Depends(get_weather_service),
        storage: BaseStorage = Depends(get_storage),
        cache: BaseCache = Depends(get_cache),
):
    if not city:
        raise HTTPException(status_code=403, detail="City name ('city') URL parameter is required.")

    filename = await cache.get_city_cache(city)
    if filename:
        print("Cache hit!", filename)
        return await storage.load(filename)

    try:
        weather_data = await weather_service.get_weather(city)
    except IncorrectCityNameError:
        raise HTTPException(status_code=403, detail="City name ('city') URL parameter is invalid.")
    except WeatherAPIError:
        raise HTTPException(status_code=500, detail="Weather service API is unavailable.")

    background_tasks.add_task(background_actions, city, weather_data, storage, cache)

    return weather_data


async def background_actions(
        city: str,
        data: dict,
        storage: BaseStorage,
        cache: BaseCache,
):
    filename = get_weather_data_filename(city)
    print("GOGO", filename)
    await storage.store(filename, data)
    await cache.set_city_cache(city, filename)



