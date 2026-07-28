from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.core.config import get_settings
from app.core.exceptions import (
    AppError,
    app_error_handler,
    unhandled_error_handler,
    validation_error_handler,
)
from app.core.logging import get_logger, setup_logging
from app.core.middleware import configure_cors
from app.api.routes.health import router as health_router
from app.api.routes.weather import router as weather_router
from app.api.routes.geocoding import router as geocoding_router
from app.api.routes.destinations import router as destinations_router
from app.api.routes.attractions import router as attractions_router
from app.api.routes.hotels import router as hotels_router
from app.api.routes.restaurants import router as restaurants_router
from app.api.routes.trip_planner import router as trip_planner_router
from app.utils.http_utils import close_http_client

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    setup_logging()
    logger.info("Starting %s", get_settings().SERVICE_NAME)
    yield
    logger.info("Shutting down %s", get_settings().SERVICE_NAME)
    await close_http_client()


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.SERVICE_NAME,
        description="Travel Planner API - aggregated travel data for destinations, weather, attractions, restaurants, hotels, and trip planning.",
        version=settings.API_VERSION,
        lifespan=lifespan,
        docs_url="/docs" if settings.is_development else None,
        redoc_url="/redoc" if settings.is_development else None,
    )

    configure_cors(app)

    app.add_exception_handler(AppError, app_error_handler)
    app.add_exception_handler(RequestValidationError, validation_error_handler)
    app.add_exception_handler(Exception, unhandled_error_handler)

    app.include_router(health_router)
    app.include_router(weather_router, prefix="/api/v1")
    app.include_router(geocoding_router, prefix="/api/v1")
    app.include_router(destinations_router, prefix="/api/v1")
    app.include_router(attractions_router, prefix="/api/v1")
    app.include_router(hotels_router, prefix="/api/v1")
    app.include_router(restaurants_router, prefix="/api/v1")
    app.include_router(trip_planner_router, prefix="/api/v1")

    return app


app = create_app()
