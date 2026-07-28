from fastapi import APIRouter, Path, Query

from app.core.logging import get_logger
from app.schemas.restaurant import RestaurantsResponse
from app.services.restaurant_service import get_restaurants_for_destination
from app.utils.response_utils import success_response

router = APIRouter(prefix="/destinations", tags=["Restaurants"])
logger = get_logger(__name__)


@router.get("/{destination_id}/restaurants", response_model=RestaurantsResponse)
async def get_restaurants(
    destination_id: str = Path(..., description="Destination slug, e.g. paris-france"),
    limit: int = Query(default=8, ge=1, le=20, description="Maximum results (1-20)"),
    cuisine: str | None = Query(default=None, description="Cuisine filter, e.g. Italian, Sushi"),
):
    """Retrieve nearby restaurants for a destination."""
    logger.info(
        "GET /destinations/%s/restaurants limit=%d cuisine=%s",
        destination_id, limit, cuisine,
    )

    restaurants = await get_restaurants_for_destination(
        destination_id=destination_id,
        limit=limit,
        cuisine=cuisine,
    )

    return success_response(
        data={"restaurants": [r.model_dump() for r in restaurants]},
        message="Restaurants retrieved successfully",
    )
