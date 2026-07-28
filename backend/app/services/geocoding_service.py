import time

from app.core.logging import get_logger
from app.schemas.geocoding import GeocodingResult
from app.integrations.providers.nominatim_client import search_places

logger = get_logger(__name__)

_SEARCH_CACHE_TTL = 600
_SEARCH_CACHE_MAX_SIZE = 500
_search_cache: dict[str, dict] = {}


def _get_cached_search(cache_key: str) -> list[dict] | None:
    entry = _search_cache.get(cache_key)
    if entry and time.monotonic() - entry["timestamp"] < _SEARCH_CACHE_TTL:
        return entry["data"]
    return None


def _set_search_cache(cache_key: str, data: list[dict]) -> None:
    if len(_search_cache) >= _SEARCH_CACHE_MAX_SIZE:
        logger.debug("Geocode cache full — clearing %d entries", len(_search_cache))
        _search_cache.clear()
    _search_cache[cache_key] = {"data": data, "timestamp": time.monotonic()}


def _build_cache_key(query: str, limit: int, country_code: str | None) -> str:
    return f"{query}:{limit}:{country_code or ''}"


def _to_geocoding_result(place: dict) -> GeocodingResult:
    return GeocodingResult(
        id=place["place_id"],
        name=place["name"],
        display_name=place["display_name"],
        latitude=place["latitude"],
        longitude=place["longitude"],
        country=place["country"],
        country_code=place["country_code"],
        region=place["region"],
        city=place["city"],
        place_type=place["place_type"],
        importance=place["importance"],
    )


async def search_locations(
    query: str,
    limit: int = 10,
    country_code: str | None = None,
) -> list[GeocodingResult]:
    """Search for locations and return normalized geocoding results."""
    logger.info("Geocoding search: query='%s' limit=%d country=%s", query, limit, country_code)

    cache_key = _build_cache_key(query, limit, country_code)
    cached = _get_cached_search(cache_key)
    if cached:
        logger.debug("Geocoding cache hit for '%s'", query)
        return [_to_geocoding_result(p) for p in cached]

    raw_results = await search_places(query=query, limit=limit, country_code=country_code)
    _set_search_cache(cache_key, raw_results)

    results = [_to_geocoding_result(p) for p in raw_results]
    logger.info("Geocoding returned %d results for '%s'", len(results), query)
    return results
