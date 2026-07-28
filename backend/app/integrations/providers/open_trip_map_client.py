from app.core.config import get_settings
from app.core.exceptions import UpstreamProviderError
from app.core.logging import get_logger
from app.utils.http_utils import http_get

logger = get_logger(__name__)

OTM_BASE_URL = "https://api.opentripmap.com/0.1/en/places"


def _get_api_key() -> str:
    return get_settings().OPENTRIPMAP_API_KEY


async def get_nearby_places(
    lat: float,
    lon: float,
    radius: int = 1000,
    limit: int = 10,
    kinds: str | None = None,
    rate: int = 1,
) -> list[dict]:
    """Fetch nearby places from OpenTripMap radius endpoint.

    Args:
        lat: Latitude of search center.
        lon: Longitude of search center.
        radius: Search radius in meters (default 1000).
        limit: Max results to return.
        kinds: Comma-separated kind filter (e.g. "museums,monuments").
        rate: Minimum quality rate 0-3 (0=all, 3=best).

    Returns:
        List of raw place dicts from OTM.
    """
    api_key = _get_api_key()
    if not api_key:
        logger.warning("OPENTRIPMAP_API_KEY not configured — returning empty results")
        return []

    params: dict = {
        "apikey": api_key,
        "lat": lat,
        "lon": lon,
        "radius": radius,
        "limit": limit,
        "rate": rate,
        "format": "json",
    }
    if kinds:
        params["kinds"] = kinds

    try:
        data = await http_get(f"{OTM_BASE_URL}/radius", params=params)
    except Exception as exc:
        logger.error("OpenTripMap radius request failed: %s", exc)
        raise UpstreamProviderError("Attractions service is temporarily unavailable") from exc

    return data if isinstance(data, list) else []


async def get_place_details(xid: str) -> dict:
    """Fetch detailed information for a single place by its xid.

    Returns:
        Raw place detail dict from OTM, or empty dict if not found.
    """
    api_key = _get_api_key()
    if not api_key:
        return {}

    try:
        data = await http_get(f"{OTM_BASE_URL}/xid/{xid}", params={"apikey": api_key})
    except Exception as exc:
        logger.error("OpenTripMap xid request failed for '%s': %s", xid, exc)
        return {}

    return data if isinstance(data, dict) else {}
