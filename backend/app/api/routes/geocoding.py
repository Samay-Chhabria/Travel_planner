from fastapi import APIRouter, Query

from app.core.logging import get_logger
from app.schemas.geocoding import GeocodingResponse
from app.services.geocoding_service import search_locations as _search_locations
from app.utils.response_utils import success_response

router = APIRouter(prefix="/geocoding", tags=["Geocoding"])
logger = get_logger(__name__)


@router.get("/search", response_model=GeocodingResponse)
async def search_locations(
    q: str = Query(..., min_length=2, description="Search query, minimum 2 characters"),
    country: str | None = Query(default=None, description="ISO 3166-1 alpha-2 country code filter"),
    limit: int = Query(default=10, ge=1, le=25, description="Maximum results (1-25)"),
    page: int = Query(default=1, ge=1, description="Page number"),
):
    """Search for locations by name. Returns geocoded results with coordinates."""
    logger.info("GET /geocoding/search q='%s' country=%s limit=%d page=%d", q, country, limit, page)

    all_results = await _search_locations(query=q, limit=25, country_code=country)

    total = len(all_results)
    start = (page - 1) * limit
    end = start + limit
    page_results = all_results[start:end]

    return success_response(
        data={
            "results": [r.model_dump() for r in page_results],
            "query": q,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
            },
        },
        message="Locations retrieved successfully",
    )
