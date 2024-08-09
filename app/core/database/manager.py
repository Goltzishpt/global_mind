from playhouse.migrate import *
from playhouse.postgres_ext import PostgresqlExtDatabase

from settings import DatabaseSettings


class DatabaseManager:
    def __init__(self, settings: DatabaseSettings):
        self.database = PostgresqlExtDatabase(
            settings.db_name, user=settings.db_user,
            password=settings.db_password, host=settings.db_host,
            port=settings.db_port
        )

    def create_tables(self, *args):
        with self.database:
            self.database.create_tables(args)


settings_db = DatabaseSettings()
db = DatabaseManager(settings_db)
