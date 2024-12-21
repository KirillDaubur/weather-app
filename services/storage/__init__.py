from services.storage.base_storage import BaseStorage
from services.storage.local_file_storage.local_file_storage import LocalFileStorage
from services.storage.s3.s3_storage import S3Storage


class StorageSingleton:
    _instance: BaseStorage = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            # If you want to replace S3 storage with local storage,
            # cls._instance = LocalFileStorage()
            cls._instance = S3Storage()

        return cls._instance

def get_storage():
    return StorageSingleton.get_instance()