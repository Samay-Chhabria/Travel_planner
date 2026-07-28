from app.core.logging import get_logger
from app.schemas.restaurant import Restaurant
from app.integrations.providers.open_trip_map_client import get_nearby_places
from app.services.destination_service import get_destination_by_id
from app.utils.converters import rate_to_price_level

logger = get_logger(__name__)


def _normalize_place(raw: dict) -> Restaurant:
    point = raw.get("point", {})
    rate = raw.get("rate", 0)
    kinds = raw.get("kinds", "")
    return Restaurant(
        id=raw.get("xid", ""),
        name=raw.get("name", "Unnamed"),
        description="",
        address="",
        latitude=point.get("lat", 0.0),
        longitude=point.get("lon", 0.0),
        image_url="",
        rating=round(rate * 5.0 / 3.0, 1) if rate > 0 else 0.0,
        cuisine_type=_extract_cuisine(kinds),
        price_level=rate_to_price_level(rate),
    )


def _extract_cuisine(kinds_str: str) -> str:
    """Extract cuisine hint from OTM kinds string."""
    if not kinds_str:
        return ""
    parts = [k.strip() for k in kinds_str.split(",")]
    food_parts = [p for p in parts if p not in ("foods",)]
    return food_parts[0].title() if food_parts else ""


async def get_restaurants_for_destination(
    destination_id: str,
    limit: int = 8,
    cuisine: str | None = None,
) -> list[Restaurant]:
    """Fetch nearby restaurants for a destination.

    Resolves the destination to coordinates, queries OpenTripMap for
    nearby food-related places, and normalizes the results.

    Args:
        destination_id: Destination slug or id (e.g. "paris-france").
        limit: Max restaurants to return (1-20).
        cuisine: Optional cuisine filter (case-insensitive).

    Returns:
        List of Restaurant objects.
    """
    logger.info(
        "Restaurant search: destination='%s' limit=%d cuisine=%s",
        destination_id, limit, cuisine,
    )

    destination = await get_destination_by_id(destination_id)

    raw_places = await get_nearby_places(
        lat=destination.latitude,
        lon=destination.longitude,
        radius=2000,
        limit=min(limit * 3, 50),
        kinds="foods",
        rate=0,
    )

    restaurants = [_normalize_place(p) for p in raw_places]

    if cuisine:
        c_lower = cuisine.lower()
        restaurants = [
            r for r in restaurants
            if c_lower in r.cuisine_type.lower() or c_lower in r.name.lower()
        ]

    return restaurants[:limit]
