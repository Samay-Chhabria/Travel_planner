from fastapi import APIRouter, Path, Query

from app.core.logging import get_logger
from app.schemas.weather import WeatherResponse
from app.services.weather_service import get_weather_for_destination
from app.utils.response_utils import success_response

router = APIRouter(prefix="/destinations", tags=["Weather"])
logger = get_logger(__name__)


@router.get("/{destination_id}/weather", response_model=WeatherResponse)
async def get_weather(
    destination_id: str = Path(..., description="Destination slug, e.g. paris-france"),
    days: int = Query(default=5, ge=1, le=16, description="Number of forecast days (1-16)"),
):
    """Return current weather and daily forecast for a destination."""
    logger.info("GET /destinations/%s/weather days=%d", destination_id, days)

    weather_data = await get_weather_for_destination(destination_id=destination_id, days=days)

    return success_response(
        data={"weather": weather_data.model_dump()},
        message="Weather data retrieved successfully",
    )
