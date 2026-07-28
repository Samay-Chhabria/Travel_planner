from app.core.logging import get_logger
from app.schemas.hotel import Hotel
from app.integrations.providers.open_trip_map_client import get_nearby_places
from app.services.destination_service import get_destination_by_id
from app.utils.converters import rate_to_price_level

logger = get_logger(__name__)

_BUDGET_MAP: dict[str, str] = {
    "budget": "budget",
    "low": "budget",
    "cheap": "budget",
    "mid": "mid_range",
    "moderate": "mid_range",
    "mid_range": "mid_range",
    "medium": "mid_range",
    "luxury": "luxury",
    "high": "luxury",
    "premium": "luxury",
    "upscale": "luxury",
}


def _rate_to_stars(rate: int) -> int:
    if rate <= 0:
        return 0
    if rate == 1:
        return 2
    if rate == 2:
        return 3
    return 5


def _normalize_place(raw: dict) -> Hotel:
    point = raw.get("point", {})
    rate = raw.get("rate", 0)
    return Hotel(
        id=raw.get("xid", ""),
        name=raw.get("name", "Unnamed"),
        description="",
        address="",
        latitude=point.get("lat", 0.0),
        longitude=point.get("lon", 0.0),
        image_url="",
        rating=round(rate * 5.0 / 3.0, 1) if rate > 0 else 0.0,
        price_level=rate_to_price_level(rate),
        star_rating=_rate_to_stars(rate),
    )


async def get_hotels_for_destination(
    destination_id: str,
    limit: int = 6,
    budget: str | None = None,
) -> list[Hotel]:
    """Fetch nearby hotels for a destination.

    Resolves the destination to coordinates, queries OpenTripMap for
    nearby accommodations, and normalizes the results.

    Args:
        destination_id: Destination slug or id (e.g. "paris-france").
        limit: Max hotels to return (1-20).
        budget: Optional budget filter ("budget", "mid_range", "luxury").

    Returns:
        List of Hotel objects.
    """
    logger.info(
        "Hotel search: destination='%s' limit=%d budget=%s",
        destination_id, limit, budget,
    )

    destination = await get_destination_by_id(destination_id)

    raw_places = await get_nearby_places(
        lat=destination.latitude,
        lon=destination.longitude,
        radius=3000,
        limit=min(limit * 3, 50),
        kinds="accomodations",
        rate=0,
    )

    hotels = [_normalize_place(p) for p in raw_places]

    if budget:
        target = _BUDGET_MAP.get(budget.lower(), budget.lower())
        hotels = [h for h in hotels if h.price_level == target]

    return hotels[:limit]
