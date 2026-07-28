import pytest
from unittest.mock import patch, AsyncMock

from app.schemas.destination import Destination


MOCK_DESTINATION = Destination(
    id="paris-france",
    name="Paris",
    country="France",
    slug="paris-france",
    latitude=48.8566,
    longitude=2.3522,
)

MOCK_OTM_HOTELS = [
    {
        "xid": "h12345",
        "name": "Grand Hotel Paris",
        "dist": 500.0,
        "rate": 3,
        "kinds": "accomodations",
        "point": {"lon": 2.3376, "lat": 48.8606},
    },
    {
        "xid": "h67890",
        "name": "Budget Inn",
        "dist": 200.0,
        "rate": 1,
        "kinds": "accomodations",
        "point": {"lon": 2.34, "lat": 48.85},
    },
    {
        "xid": "h11111",
        "name": "Mid Stay Hotel",
        "dist": 300.0,
        "rate": 2,
        "kinds": "accomodations",
        "point": {"lon": 2.35, "lat": 48.86},
    },
]


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_HOTELS)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_hotels_success(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/hotels")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Hotels retrieved successfully"

    data = body["data"]
    assert len(data["hotels"]) == 3
    assert data["hotels"][0]["name"] == "Grand Hotel Paris"
    assert data["hotels"][0]["price_level"] == "luxury"
    assert data["hotels"][0]["star_rating"] == 5
    assert data["hotels"][1]["name"] == "Budget Inn"
    assert data["hotels"][1]["price_level"] == "budget"
    assert data["hotels"][1]["star_rating"] == 2


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_HOTELS)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_hotels_with_limit(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/hotels?limit=2")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["hotels"]) == 2


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_HOTELS)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_hotels_budget_filter(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/hotels?budget=budget")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["hotels"]) == 1
    assert body["data"]["hotels"][0]["name"] == "Budget Inn"


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_HOTELS)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_hotels_luxury_filter(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/hotels?budget=luxury")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["hotels"]) == 1
    assert body["data"]["hotels"][0]["name"] == "Grand Hotel Paris"


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_HOTELS)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_hotels_budget_alias(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/hotels?budget=low")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["hotels"]) == 1
    assert body["data"]["hotels"][0]["name"] == "Budget Inn"


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock, return_value=[])
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_hotels_empty(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/hotels")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["hotels"] == []


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_hotels_destination_not_found(mock_dest, mock_otm, client):
    from app.core.exceptions import NotFoundError

    mock_dest.side_effect = NotFoundError("Destination not found for 'nowhere-xx'")

    response = await client.get("/api/v1/destinations/nowhere-xx/hotels")

    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "NOT_FOUND"


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_hotels_upstream_failure(mock_dest, mock_otm, client):
    from app.core.exceptions import UpstreamProviderError

    mock_otm.side_effect = UpstreamProviderError("Attractions service is temporarily unavailable")

    response = await client.get("/api/v1/destinations/paris-france/hotels")

    assert response.status_code == 502
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "UPSTREAM_PROVIDER_ERROR"


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_HOTELS)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_hotels_response_fields(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/hotels?limit=1")

    assert response.status_code == 200
    result = response.json()["data"]["hotels"][0]
    expected_fields = {
        "id", "name", "description", "address", "latitude", "longitude",
        "image_url", "rating", "price_level", "star_rating",
    }
    assert expected_fields == set(result.keys())


@pytest.mark.asyncio
async def test_get_hotels_invalid_limit_too_low(client):
    response = await client.get("/api/v1/destinations/paris-france/hotels?limit=0")
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_hotels_invalid_limit_too_high(client):
    response = await client.get("/api/v1/destinations/paris-france/hotels?limit=50")
    assert response.status_code == 422
