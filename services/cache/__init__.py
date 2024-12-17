from services.cache.aiocache.aiocache import AIOCache
from services.cache.base_cache import BaseCache


class CacheSingleton:
    _instance: BaseCache = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = AIOCache()

        return cls._instance

def get_cache():
    return CacheSingleton.get_instance()