from aiocache import Cache

from services.cache.base_cache import BaseCache
from settings import Settings, get_settings
from utils import get_file_entry_cache_key


class AIOCache(BaseCache):
    def __init__(self, settings: Settings = get_settings()):
        self.client = Cache(
            cache_class=Cache.MEMCACHED,
            endpoint=settings.memcached_host,
            port=settings.memcached_port
        )
        self.ttl = settings.cache_city_entries_expiration_seconds

    async def get_city_cache(self, city: str):
        print("obtaining", get_file_entry_cache_key(city))
        return await self.client.get(get_file_entry_cache_key(city))

    async def set_city_cache(self, city: str, value: str):
        print("stored", get_file_entry_cache_key(city))
        await self.client.set(get_file_entry_cache_key(city), value, ttl=self.ttl)

