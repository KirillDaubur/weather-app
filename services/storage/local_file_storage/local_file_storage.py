import json
from pathlib import Path

import aiofiles

from services.storage.base_storage import BaseStorage
from settings import Settings, get_settings


class LocalFileStorage(BaseStorage):

    def __init__(self, settings: Settings = get_settings()):
        self.base_path: Path = settings.local_file_storage_base_path / ".storage"


    async def store(self, filename: str, data: dict) -> None:
        filepath = self.base_path / filename

        self.base_path.mkdir(parents=True, exist_ok=True)

        async with aiofiles.open(filepath, mode="w") as file:
            await file.write(json.dumps(data, indent=4))


    async def load(self, filename: str) -> dict:
        if not self.base_path.exists():
            raise FileNotFoundError

        filepath = self.base_path / filename

        async with aiofiles.open(filepath, mode="r") as file:
            content = await file.read()
            return json.loads(content)
