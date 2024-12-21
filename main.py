import time
from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends, HTTPException, BackgroundTasks

from errors import IncorrectCityNameError, WeatherAPIError
from services.cache import BaseCache, get_cache
from services.db import BaseDB, get_db
from services.storage import BaseStorage, get_storage
from services.weather_service import get_weather_service
from services.weather_service.base_weather_service import BaseWeatherService
from utils import get_weather_data_filename


@asynccontextmanager
async def lifespan(app: FastAPI, db: BaseDB = get_db()):
    await db.init_db()
    print("DB initiated")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/weather")
async def weather(
        background_tasks: BackgroundTasks,
        city: str = "",
        weather_service: BaseWeatherService = Depends(get_weather_service),
        storage: BaseStorage = Depends(get_storage),
        cache: BaseCache = Depends(get_cache),
        db: BaseDB = Depends(get_db)
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

    background_tasks.add_task(background_actions, city, weather_data, storage, cache, db)

    return weather_data


async def background_actions(
        city: str,
        data: dict,
        storage: BaseStorage,
        cache: BaseCache,
        db: BaseDB
):
    filename = get_weather_data_filename(city)
    print("GOGO", filename)
    await storage.store(filename, data)
    await cache.set_city_cache(city, filename)
    await db.save_log_entry(city, round(time.time() * 1000), filename)



