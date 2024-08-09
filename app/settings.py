from pydantic_settings import BaseSettings


class DatabaseSettings(BaseSettings):
    db_name: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int

    class Config:
        env_file = ".env"


class ServerSettings(BaseSettings):
    host: str
    port: int

    class Config:
        env_file = ".env"
