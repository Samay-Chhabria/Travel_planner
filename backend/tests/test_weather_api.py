import pytest
from unittest.mock import patch, AsyncMock

from app.core.exceptions import NotFoundError, UpstreamProviderError


@pytest.fixture(autouse=True)
def _clear_geocode_cache():
    """Ensure a clean geocode cache for each test."""
    with patch("app.services.weather_service._geocode_cache", {}):
        yield


MOCK_OPEN_METEO_RESPONSE = {
    "latitude": 48.86,
    "longitude": 2.36,
    "current": {
        "time": "2026-07-13T10:30",
        "temperature_2m": 27.7,
        "weather_code": 3,
        "relative_humidity_2m": 39,
        "wind_speed_10m": 13.5,
    },
    "daily": {
        "time": ["2026-07-13", "2026-07-14", "2026-07-15"],
        "temperature_2m_max": [35.1, 35.1, 32.4],
        "temperature_2m_min": [22.5, 22.0, 24.8],
        "weather_code": [80, 3, 3],
    },
}

MOCK_GEO = {"latitude": 48.8566, "longitude": 2.3522, "display_name": "Paris, France"}


@pytest.mark.asyncio
@patch("app.services.weather_service.geocode_place", new_callable=AsyncMock, return_value=MOCK_GEO)
@patch("app.services.weather_service.fetch_current_and_forecast", new_callable=AsyncMock, return_value=MOCK_OPEN_METEO_RESPONSE)
async def test_get_weather_success(mock_fetch, mock_geo, client):
    response = await client.get("/api/v1/destinations/paris-france/weather")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Weather data retrieved successfully"

    weather = body["data"]["weather"]
    assert weather["destination_id"] == "paris-france"
    assert "current" in weather
    assert "forecast" in weather
    assert weather["current"]["temperature_c"] == 27.7
    assert weather["current"]["temperature_f"] == 81.9
    assert weather["current"]["condition"] == "Overcast"
    assert len(weather["forecast"]) == 3


@pytest.mark.asyncio
@patch("app.services.weather_service.geocode_place", new_callable=AsyncMock, return_value=MOCK_GEO)
@patch("app.services.weather_service.fetch_current_and_forecast", new_callable=AsyncMock, return_value=MOCK_OPEN_METEO_RESPONSE)
async def test_get_weather_with_days_param(mock_fetch, mock_geo, client):
    response = await client.get("/api/v1/destinations/paris-france/weather?days=7")

    assert response.status_code == 200
    mock_fetch.assert_called_once_with(latitude=48.8566, longitude=2.3522, forecast_days=7)


@pytest.mark.asyncio
async def test_get_weather_invalid_days_too_low(client):
    response = await client.get("/api/v1/destinations/paris-france/weather?days=0")
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_weather_invalid_days_too_high(client):
    response = await client.get("/api/v1/destinations/paris-france/weather?days=20")
    assert response.status_code == 422


@pytest.mark.asyncio
@patch("app.services.weather_service.geocode_place", new_callable=AsyncMock, return_value=MOCK_GEO)
@patch("app.services.weather_service.fetch_current_and_forecast", new_callable=AsyncMock)
async def test_get_weather_upstream_failure(mock_fetch, mock_geo, client):
    mock_fetch.side_effect = UpstreamProviderError("Weather provider is temporarily unavailable")

    response = await client.get("/api/v1/destinations/paris-france/weather")

    assert response.status_code == 502
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "UPSTREAM_PROVIDER_ERROR"


@pytest.mark.asyncio
@patch("app.services.weather_service.geocode_place", new_callable=AsyncMock)
async def test_get_weather_location_not_found(mock_geo, client):
    mock_geo.side_effect = NotFoundError("Location not found for 'Unknownplace'")

    response = await client.get("/api/v1/destinations/unknownplace/weather")

    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "NOT_FOUND"
