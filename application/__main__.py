from fastapi import FastAPI
from sqlalchemy import select

from config import Settings, get_settings
from db.connection import get_session
from db.models import Model
from endpoints import list_of_routes

from uvicorn import run


def bind_routes(application: FastAPI, setting: Settings) -> None:
    """
    Bind all routes to application.
    """
    for route in list_of_routes:
        application.include_router(route, prefix=setting.PATH_PREFIX)


def get_app() -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = "Микросервис"

    session = get_session()

    session.scalar(select(Model))

    tags_metadata = [
        {
            "name": "Application Health",
            "description": "API health check.",
        },
    ]

    application = FastAPI(
        title="app",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="0.1.0",
        openapi_tags=tags_metadata,
    )
    settings = get_settings()
    bind_routes(application, settings)
    application.state.settings = settings
    return application


app = get_app()

if __name__ == "__main__":
    settings_for_application = get_settings()
    run(
        "__main__:app",
        port=settings_for_application.APP_PORT,
        reload=True,
        reload_dirs=["bookmarker", "tests"],
        log_level="debug",
    )
