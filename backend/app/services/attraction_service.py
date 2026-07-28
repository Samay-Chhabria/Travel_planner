from app.core.logging import get_logger
from app.schemas.attraction import Attraction
from app.integrations.providers.open_trip_map_client import get_nearby_places
from app.services.destination_service import get_destination_by_id

logger = get_logger(__name__)

_CATEGORY_MAP: dict[str, str] = {
    "cultural": "Culture",
    "museums": "Museum",
    "monuments": "Monument",
    "architecture": "Architecture",
    "natural": "Nature",
    "geological_formations": "Nature",
    "foods": "Food",
    "shops": "Shopping",
    "amusements": "Entertainment",
    "transport": "Transport",
    "accomodations": "Hotel",
    "urban_environment": "Urban",
    "religion": "Religion",
    "sport": "Sport",
    "historical_places": "History",
    "other": "Other",
}


def _primary_category(kinds_str: str) -> str:
    """Extract the first kind from OTM's comma-separated kinds string and map to a label."""
    if not kinds_str:
        return ""
    first = kinds_str.split(",")[0].strip().lower()
    return _CATEGORY_MAP.get(first, first.title())


def _otm_rate_to_five(rate: int) -> float:
    """Scale OTM rate (0-3) to a 0-5 scale."""
    return round(rate * 5.0 / 3.0, 1) if rate > 0 else 0.0


def _normalize_place(raw: dict) -> Attraction:
    point = raw.get("point", {})
    return Attraction(
        id=raw.get("xid", ""),
        name=raw.get("name", "Unnamed"),
        category=_primary_category(raw.get("kinds", "")),
        description="",
        address="",
        latitude=point.get("lat", 0.0),
        longitude=point.get("lon", 0.0),
        image_url="",
        rating=_otm_rate_to_five(raw.get("rate", 0)),
    )


async def get_attractions_for_destination(
    destination_id: str,
    limit: int = 8,
    category: str | None = None,
) -> list[Attraction]:
    """Fetch nearby attractions for a destination.

    Resolves the destination to coordinates, queries OpenTripMap for nearby
    places, and normalizes the results.

    Args:
        destination_id: Destination slug or id (e.g. "paris-france").
        limit: Max attractions to return (1-20).
        category: Optional category filter (case-insensitive).

    Returns:
        List of Attraction objects.
    """
    logger.info(
        "Attraction search: destination='%s' limit=%d category=%s",
        destination_id, limit, category,
    )

    destination = await get_destination_by_id(destination_id)

    raw_places = await get_nearby_places(
        lat=destination.latitude,
        lon=destination.longitude,
        radius=2000,
        limit=min(limit * 2, 50),
        rate=1,
    )

    attractions = [_normalize_place(p) for p in raw_places]

    if category:
        cat_lower = category.lower()
        attractions = [a for a in attractions if cat_lower in a.category.lower()]

    return attractions[:limit]
