from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openweathermap_app_id: str
    local_file_storage_base_path: Path = Path(__file__).resolve().parent
    database_url: str = "sqlite:///./test.db"

    memcached_host: str = "memcached"
    memcached_port: int = 11211
    cache_city_entries_expiration_seconds: int = 60 * 5

    model_config = SettingsConfigDict(env_file=".env")

class SettingsSingleton:
    _instance: Settings = None

    @classmethod
    def get_instance(cls) -> Settings:
        if cls._instance is None:
            cls._instance = Settings()
        return cls._instance

def get_settings() -> Settings:
    return SettingsSingleton.get_instance()