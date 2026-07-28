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

MOCK_OTM_RESTAURANTS = [
    {
        "xid": "r12345",
        "name": "Le Petit Bistro",
        "dist": 400.0,
        "rate": 3,
        "kinds": "foods,restaurants",
        "point": {"lon": 2.3376, "lat": 48.8606},
    },
    {
        "xid": "r67890",
        "name": "Corner Cafe",
        "dist": 200.0,
        "rate": 1,
        "kinds": "foods",
        "point": {"lon": 2.34, "lat": 48.85},
    },
    {
        "xid": "r11111",
        "name": "Sakura Sushi",
        "dist": 300.0,
        "rate": 2,
        "kinds": "foods,restaurants",
        "point": {"lon": 2.35, "lat": 48.86},
    },
]


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_RESTAURANTS)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_restaurants_success(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/restaurants")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Restaurants retrieved successfully"

    data = body["data"]
    assert len(data["restaurants"]) == 3
    assert data["restaurants"][0]["name"] == "Le Petit Bistro"
    assert data["restaurants"][0]["price_level"] == "luxury"
    assert data["restaurants"][1]["name"] == "Corner Cafe"
    assert data["restaurants"][1]["price_level"] == "budget"


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_RESTAURANTS)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_restaurants_with_limit(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/restaurants?limit=2")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["restaurants"]) == 2


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_RESTAURANTS)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_restaurants_cuisine_filter(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/restaurants?cuisine=bistro")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["restaurants"]) == 1
    assert body["data"]["restaurants"][0]["name"] == "Le Petit Bistro"


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_RESTAURANTS)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_restaurants_cuisine_no_match(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/restaurants?cuisine=chinese")

    assert response.status_code == 200
    body = response.json()
    assert body["data"]["restaurants"] == []


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock, return_value=[])
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_restaurants_empty(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/restaurants")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["restaurants"] == []


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_restaurants_destination_not_found(mock_dest, mock_otm, client):
    from app.core.exceptions import NotFoundError

    mock_dest.side_effect = NotFoundError("Destination not found for 'nowhere-xx'")

    response = await client.get("/api/v1/destinations/nowhere-xx/restaurants")

    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "NOT_FOUND"


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_restaurants_upstream_failure(mock_dest, mock_otm, client):
    from app.core.exceptions import UpstreamProviderError

    mock_otm.side_effect = UpstreamProviderError("Attractions service is temporarily unavailable")

    response = await client.get("/api/v1/destinations/paris-france/restaurants")

    assert response.status_code == 502
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "UPSTREAM_PROVIDER_ERROR"


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_RESTAURANTS)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_restaurants_response_fields(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/restaurants?limit=1")

    assert response.status_code == 200
    result = response.json()["data"]["restaurants"][0]
    expected_fields = {
        "id", "name", "description", "address", "latitude", "longitude",
        "image_url", "rating", "cuisine_type", "price_level",
    }
    assert expected_fields == set(result.keys())


@pytest.mark.asyncio
async def test_get_restaurants_invalid_limit_too_low(client):
    response = await client.get("/api/v1/destinations/paris-france/restaurants?limit=0")
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_restaurants_invalid_limit_too_high(client):
    response = await client.get("/api/v1/destinations/paris-france/restaurants?limit=50")
    assert response.status_code == 422
