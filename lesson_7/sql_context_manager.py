import sqlite3


class DataBaseManager:

    def __init__(self, db_name: str):
        self._db_name = db_name

    def __enter__(self):
        self._connect = sqlite3.connect(self._db_name)
        self._cursor = self._connect.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._connect.commit()
        self._connect.close()
