import time

from app.core.logging import get_logger
from app.schemas.weather import CurrentWeather, ForecastDay, WeatherData
from app.integrations.providers.open_meteo_client import decode_weather_code, fetch_current_and_forecast
from app.integrations.providers.nominatim_client import geocode_place

logger = get_logger(__name__)

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_TO_FAHRENHEIT_OFFSET = 32

_GEOCODE_CACHE_TTL = 3600
_GEOCODE_CACHE_MAX_SIZE = 200
_geocode_cache: dict[str, dict] = {}


def _get_cached_geocode(query: str) -> dict | None:
    entry = _geocode_cache.get(query)
    if entry and time.monotonic() - entry["timestamp"] < _GEOCODE_CACHE_TTL:
        return entry["data"]
    return None


def _set_geocode_cache(query: str, data: dict) -> None:
    if len(_geocode_cache) >= _GEOCODE_CACHE_MAX_SIZE:
        logger.debug("Weather geocode cache full — clearing %d entries", len(_geocode_cache))
        _geocode_cache.clear()
    _geocode_cache[query] = {"data": data, "timestamp": time.monotonic()}


def _celsius_to_fahrenheit(celsius: float) -> float:
    return round(celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + CELSIUS_TO_FAHRENHEIT_OFFSET, 1)


def _normalize_current(raw_current: dict) -> CurrentWeather:
    code = raw_current.get("weather_code", 0)
    weather_info = decode_weather_code(code)
    temp_c = raw_current.get("temperature_2m", 0)

    return CurrentWeather(
        temperature_c=round(temp_c, 1),
        temperature_f=_celsius_to_fahrenheit(temp_c),
        condition=weather_info["condition"],
        description=weather_info["description"],
    )


def _normalize_forecast(raw_daily: dict) -> list[ForecastDay]:
    dates = raw_daily.get("time", [])
    max_temps = raw_daily.get("temperature_2m_max", [])
    min_temps = raw_daily.get("temperature_2m_min", [])
    codes = raw_daily.get("weather_code", [])

    forecast = []
    for i, date_str in enumerate(dates):
        code = codes[i] if i < len(codes) else 0
        weather_info = decode_weather_code(code)
        forecast.append(
            ForecastDay(
                date=date_str,
                max_temp_c=round(max_temps[i], 1) if i < len(max_temps) else 0,
                min_temp_c=round(min_temps[i], 1) if i < len(min_temps) else 0,
                condition=weather_info["condition"],
            )
        )

    return forecast


async def get_weather_for_destination(destination_id: str, days: int = 5) -> WeatherData:
    """Resolve a destination slug to coordinates and fetch normalized weather data."""
    logger.info("Fetching weather for destination_id=%s days=%d", destination_id, days)

    slug_parts = destination_id.split("-")
    query = " ".join(part.capitalize() for part in slug_parts)

    cached = _get_cached_geocode(query)
    if cached:
        logger.debug("Geocode cache hit for '%s'", query)
        location = cached
    else:
        location = await geocode_place(query)
        _set_geocode_cache(query, location)

    raw_weather = await fetch_current_and_forecast(
        latitude=location["latitude"],
        longitude=location["longitude"],
        forecast_days=days,
    )

    current = _normalize_current(raw_weather.get("current", {}))
    forecast = _normalize_forecast(raw_weather.get("daily", {}))

    weather_data = WeatherData(
        destination_id=destination_id,
        current=current,
        forecast=forecast,
    )

    logger.info("Weather data normalized for destination_id=%s", destination_id)
    return weather_data
