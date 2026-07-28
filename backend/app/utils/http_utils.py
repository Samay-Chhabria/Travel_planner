import httpx

from app.core.config import get_settings
from app.core.logging import get_logger

logger = get_logger(__name__)

_http_client: httpx.AsyncClient | None = None


async def get_http_client() -> httpx.AsyncClient:
    global _http_client
    settings = get_settings()
    if _http_client is None or _http_client.is_closed:
        _http_client = httpx.AsyncClient(
            timeout=httpx.Timeout(settings.HTTP_TIMEOUT),
            follow_redirects=True,
        )
        logger.info("HTTP client initialized")
    return _http_client


async def close_http_client() -> None:
    global _http_client
    if _http_client is not None and not _http_client.is_closed:
        await _http_client.aclose()
        _http_client = None
        logger.info("HTTP client closed")


async def http_get(url: str, params: dict | None = None, headers: dict | None = None) -> dict | list:
    client = await get_http_client()
    safe_params = {k: ("***" if k == "apikey" else v) for k, v in (params or {}).items()}
    logger.debug("GET %s params=%s", url, safe_params)

    try:
        response = await client.get(url, params=params, headers=headers)
        response.raise_for_status()
    except httpx.TimeoutException as exc:
        logger.error("Timeout calling %s: %s", url, exc)
        raise
    except httpx.HTTPStatusError as exc:
        logger.error("HTTP %d from %s", exc.response.status_code, url)
        raise

    return response.json()
