from app.core.exceptions import NotFoundError, UpstreamProviderError
from app.core.logging import get_logger
from app.utils.http_utils import http_get

logger = get_logger(__name__)

NOMINATIM_SEARCH_URL = "https://nominatim.openstreetmap.org/search"
USER_AGENT = "travel-planner-backend/1.0"


async def geocode_place(query: str) -> dict:
    """Resolve a place name to latitude, longitude, and display name (single result)."""
    results = await search_places(query, limit=1)
    if not results:
        raise NotFoundError(f"Location not found for '{query}'")
    return results[0]


async def search_places(query: str, limit: int = 10, country_code: str | None = None) -> list[dict]:
    """Search for places matching a query string. Returns normalized result dicts."""
    params: dict = {
        "q": query,
        "format": "json",
        "limit": limit,
        "addressdetails": 1,
    }
    if country_code:
        params["countrycodes"] = country_code.lower()

    headers = {"User-Agent": USER_AGENT}

    try:
        data = await http_get(NOMINATIM_SEARCH_URL, params=params, headers=headers)
    except Exception as exc:
        logger.error("Nominatim search failed for query='%s': %s", query, exc)
        raise UpstreamProviderError("Geocoding service is temporarily unavailable") from exc

    if not data:
        return []

    return [_normalize_place(item) for item in data]


def _normalize_place(raw: dict) -> dict:
    address = raw.get("address", {})
    return {
        "place_id": str(raw.get("place_id", "")),
        "name": raw.get("name", ""),
        "display_name": raw.get("display_name", ""),
        "latitude": float(raw.get("lat", 0)),
        "longitude": float(raw.get("lon", 0)),
        "country": address.get("country", ""),
        "country_code": address.get("country_code", ""),
        "region": address.get("state", ""),
        "city": address.get("city", address.get("town", address.get("village", ""))),
        "place_type": raw.get("type", ""),
        "importance": float(raw.get("importance", 0)),
    }
