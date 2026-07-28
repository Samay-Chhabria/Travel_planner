from fastapi import APIRouter, Path, Query

from app.core.logging import get_logger
from app.schemas.destination import (
    DestinationDetailResponse,
    DestinationSearchResponse,
    FeaturedDestinationsResponse,
)
from app.services.destination_service import (
    get_destination_by_id,
    get_featured_destinations,
    search_destinations,
)
from app.utils.response_utils import success_response

router = APIRouter(prefix="/destinations", tags=["Destinations"])
logger = get_logger(__name__)


@router.get("/search", response_model=DestinationSearchResponse)
async def search(
    q: str = Query(..., min_length=2, description="Search query, minimum 2 characters"),
    country: str | None = Query(default=None, description="ISO 3166-1 alpha-2 country code filter"),
    limit: int = Query(default=10, ge=1, le=25, description="Maximum results (1-25)"),
    page: int = Query(default=1, ge=1, description="Page number"),
):
    """Search destinations by query string."""
    logger.info("GET /destinations/search q='%s' country=%s limit=%d page=%d", q, country, limit, page)

    all_results = await search_destinations(query=q, limit=25, country_code=country)

    total = len(all_results)
    start = (page - 1) * limit
    end = start + limit
    page_results = all_results[start:end]

    return success_response(
        data={
            "results": [d.model_dump() for d in page_results],
            "query": q,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
            },
        },
        message="Destinations retrieved successfully",
    )


@router.get("/featured", response_model=FeaturedDestinationsResponse)
async def featured(
    limit: int = Query(default=6, ge=1, le=20, description="Number of featured destinations (1-20)"),
):
    """Retrieve curated featured destinations for the landing page."""
    logger.info("GET /destinations/featured limit=%d", limit)

    destinations = get_featured_destinations(limit=limit)

    return success_response(
        data={"destinations": [d.model_dump() for d in destinations]},
        message="Featured destinations retrieved successfully",
    )


@router.get("/{destination_id}", response_model=DestinationDetailResponse)
async def detail(
    destination_id: str = Path(..., description="Destination id or slug, e.g. paris-france"),
):
    """Get a single destination by id or slug."""
    logger.info("GET /destinations/%s", destination_id)

    destination = await get_destination_by_id(destination_id=destination_id)

    return success_response(
        data={"destination": destination.model_dump()},
        message="Destination details retrieved successfully",
    )
