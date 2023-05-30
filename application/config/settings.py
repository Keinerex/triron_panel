from os import environ
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from pydantic import BaseSettings


class Settings(BaseSettings):
    ENV: str = environ.get("ENV", "local")
    PATH_PREFIX: str = environ.get("PATH_PREFIX", "/api/v1")
    APP_HOST: str = environ.get("APP_HOST", "http://127.0.0.1")
    APP_PORT: int = int(environ.get("APP_PORT", 8000))

    POSTGRES_DB: str = environ.get("POSTGRES_DB", "triton_storage_db")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "45.138.157.226")
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "admin")
    POSTGRES_PORT: int = int(environ.get("POSTGRES_PORT", "5432")[-4:])
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "password")
    DB_CONNECT_RETRY: int = environ.get("DB_CONNECT_RETRY", 20)
    DB_POOL_SIZE: int = environ.get("DB_POOL_SIZE", 15)

    SECRET_KEY: str = environ.get("SECRET_KEY", "ultra_super_secret_key")
    ALGORITHM: str = environ.get("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 1440))

    PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
    OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl=f"{APP_HOST}:{APP_PORT}{PATH_PREFIX}/user/authentication")

    @property
    def database_settings(self) -> dict:
        """
        Get all settings for connection with database.
        """
        return {
            "database": self.POSTGRES_DB,
            "user": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
            "host": self.POSTGRES_HOST,
            "port": self.POSTGRES_PORT,
        }

    @property
    def database_url(self) -> str:
        """
        Get url for async connection with database.
        """
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(**self.database_settings, )

    @property
    def database_url_sync(self) -> str:
        """
        Get url for connection with database.
        """
        return "postgresql://{user}:{password}@{host}:{port}/{database}".format(**self.database_settings, )


class Config:
    env_file = ".env"
    env_file_encoding = "utf-8"
