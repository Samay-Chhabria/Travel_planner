from fastapi import APIRouter, Path, Query

from app.core.logging import get_logger
from app.schemas.hotel import HotelsResponse
from app.services.hotel_service import get_hotels_for_destination
from app.utils.response_utils import success_response

router = APIRouter(prefix="/destinations", tags=["Hotels"])
logger = get_logger(__name__)


@router.get("/{destination_id}/hotels", response_model=HotelsResponse)
async def get_hotels(
    destination_id: str = Path(..., description="Destination slug, e.g. paris-france"),
    limit: int = Query(default=6, ge=1, le=20, description="Maximum results (1-20)"),
    budget: str | None = Query(default=None, description="Budget filter: budget, mid_range, luxury"),
):
    """Retrieve nearby hotels for a destination."""
    logger.info(
        "GET /destinations/%s/hotels limit=%d budget=%s",
        destination_id, limit, budget,
    )

    hotels = await get_hotels_for_destination(
        destination_id=destination_id,
        limit=limit,
        budget=budget,
    )

    return success_response(
        data={"hotels": [h.model_dump() for h in hotels]},
        message="Hotels retrieved successfully",
    )
