from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openweathermap_app_id: str
    local_file_storage_base_path: Path = Path(__file__).resolve().parent

    memcached_host: str = "memcached"
    memcached_port: int = 11211
    cache_city_entries_expiration_seconds: int = 60 * 5

    postgres_host: str
    postgres_port: str
    postgres_user: str
    postgres_password: str
    postgres_db: str

    aws_access_key_id: str
    aws_secret_access_key: str
    s3_bucket_name: str
    s3_endpoint_url: str = None

    @property
    def postgres_url(self):
        return (f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
                f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}")

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