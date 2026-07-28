from app.core.exceptions import UpstreamProviderError
from app.core.logging import get_logger
from app.utils.http_utils import http_get

logger = get_logger(__name__)

OPEN_METEO_BASE_URL = "https://api.open-meteo.com/v1/forecast"

WMO_WEATHER_CODES: dict[int, dict[str, str]] = {
    0: {"condition": "Clear", "description": "Clear sky"},
    1: {"condition": "Mostly Clear", "description": "Mainly clear"},
    2: {"condition": "Partly Cloudy", "description": "Partly cloudy"},
    3: {"condition": "Overcast", "description": "Overcast"},
    45: {"condition": "Fog", "description": "Foggy"},
    48: {"condition": "Fog", "description": "Depositing rime fog"},
    51: {"condition": "Drizzle", "description": "Light drizzle"},
    53: {"condition": "Drizzle", "description": "Moderate drizzle"},
    55: {"condition": "Drizzle", "description": "Dense drizzle"},
    61: {"condition": "Rain", "description": "Slight rain"},
    63: {"condition": "Rain", "description": "Moderate rain"},
    65: {"condition": "Rain", "description": "Heavy rain"},
    66: {"condition": "Freezing Rain", "description": "Light freezing rain"},
    67: {"condition": "Freezing Rain", "description": "Heavy freezing rain"},
    71: {"condition": "Snow", "description": "Slight snowfall"},
    73: {"condition": "Snow", "description": "Moderate snowfall"},
    75: {"condition": "Snow", "description": "Heavy snowfall"},
    77: {"condition": "Snow", "description": "Snow grains"},
    80: {"condition": "Rain Showers", "description": "Slight rain showers"},
    81: {"condition": "Rain Showers", "description": "Moderate rain showers"},
    82: {"condition": "Rain Showers", "description": "Violent rain showers"},
    85: {"condition": "Snow Showers", "description": "Slight snow showers"},
    86: {"condition": "Snow Showers", "description": "Heavy snow showers"},
    95: {"condition": "Thunderstorm", "description": "Thunderstorm"},
    96: {"condition": "Thunderstorm", "description": "Thunderstorm with slight hail"},
    99: {"condition": "Thunderstorm", "description": "Thunderstorm with heavy hail"},
}


def decode_weather_code(code: int) -> dict[str, str]:
    return WMO_WEATHER_CODES.get(code, {"condition": "Unknown", "description": "Unknown conditions"})


async def fetch_current_and_forecast(latitude: float, longitude: float, forecast_days: int = 5) -> dict:
    """Fetch current weather and daily forecast from Open-Meteo."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code,relative_humidity_2m,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,weather_code",
        "timezone": "auto",
        "forecast_days": forecast_days,
    }

    try:
        data = await http_get(OPEN_METEO_BASE_URL, params=params)
    except Exception as exc:
        logger.error("Open-Meteo request failed: %s", exc)
        raise UpstreamProviderError("Weather provider is temporarily unavailable") from exc

    return data
