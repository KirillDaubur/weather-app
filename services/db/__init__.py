from services.db.base_db import BaseDB
from services.db.sql_db.sql_db import SqlDb


class DBSingleton:
    _instance: BaseDB = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = SqlDb()

        return cls._instance

def get_db():
    return DBSingleton.get_instance()