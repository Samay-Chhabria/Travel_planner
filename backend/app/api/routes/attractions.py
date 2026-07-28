from fastapi import APIRouter, Path, Query

from app.core.logging import get_logger
from app.schemas.attraction import AttractionsResponse
from app.services.attraction_service import get_attractions_for_destination
from app.utils.response_utils import success_response

router = APIRouter(prefix="/destinations", tags=["Attractions"])
logger = get_logger(__name__)


@router.get("/{destination_id}/attractions", response_model=AttractionsResponse)
async def get_attractions(
    destination_id: str = Path(..., description="Destination slug, e.g. paris-france"),
    limit: int = Query(default=8, ge=1, le=20, description="Maximum results (1-20)"),
    category: str | None = Query(default=None, description="Category filter, e.g. Museum, Nature"),
):
    """Retrieve nearby attractions for a destination."""
    logger.info(
        "GET /destinations/%s/attractions limit=%d category=%s",
        destination_id, limit, category,
    )

    attractions = await get_attractions_for_destination(
        destination_id=destination_id,
        limit=limit,
        category=category,
    )

    return success_response(
        data={"attractions": [a.model_dump() for a in attractions]},
        message="Attractions retrieved successfully",
    )
