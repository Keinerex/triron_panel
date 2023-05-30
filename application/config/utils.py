from os import environ

from application.config.settings import Settings


def get_settings() -> Settings:
    env = environ.get("ENV", "local")
    if env == "local":
        return Settings()
    # ...
    # space for other settings
    # ...
    return Settings()  # fallback to default
