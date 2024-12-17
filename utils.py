import time


def get_file_entry_cache_key(city: str):
    return f"cache_entry_{city.lower()}"

def get_weather_data_filename(city_name: str) -> str:
    return f"{city_name.lower()}_{round(time.time() * 1000)}.json"