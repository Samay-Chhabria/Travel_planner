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

MOCK_OTM_PLACES = [
    {
        "xid": "n12345",
        "name": "Louvre Museum",
        "dist": 500.0,
        "rate": 3,
        "kinds": "museums,cultural",
        "point": {"lon": 2.3376, "lat": 48.8606},
    },
    {
        "xid": "n67890",
        "name": "Eiffel Tower",
        "dist": 3000.0,
        "rate": 3,
        "kinds": "monuments,architecture",
        "point": {"lon": 2.2945, "lat": 48.8584},
    },
    {
        "xid": "n11111",
        "name": "Bois de Boulogne",
        "dist": 4000.0,
        "rate": 2,
        "kinds": "natural",
        "point": {"lon": 2.25, "lat": 48.86},
    },
]


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_PLACES)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_attractions_success(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/attractions")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Attractions retrieved successfully"

    data = body["data"]
    assert len(data["attractions"]) == 3
    assert data["attractions"][0]["name"] == "Louvre Museum"
    assert data["attractions"][0]["category"] == "Museum"
    assert data["attractions"][0]["rating"] == 5.0
    assert data["attractions"][1]["name"] == "Eiffel Tower"
    assert data["attractions"][1]["category"] == "Monument"


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_PLACES)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_attractions_with_limit(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/attractions?limit=2")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["attractions"]) == 2


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_PLACES)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_attractions_with_category(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/attractions?category=Museum")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["attractions"]) == 1
    assert body["data"]["attractions"][0]["name"] == "Louvre Museum"


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_PLACES)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_attractions_category_no_match(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/attractions?category=Shopping")

    assert response.status_code == 200
    body = response.json()
    assert body["data"]["attractions"] == []


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock, return_value=[])
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_attractions_empty(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/attractions")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["attractions"] == []


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_attractions_destination_not_found(mock_dest, mock_otm, client):
    from app.core.exceptions import NotFoundError

    mock_dest.side_effect = NotFoundError("Destination not found for 'nowhere-xx'")

    response = await client.get("/api/v1/destinations/nowhere-xx/attractions")

    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "NOT_FOUND"


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_attractions_upstream_failure(mock_dest, mock_otm, client):
    from app.core.exceptions import UpstreamProviderError

    mock_otm.side_effect = UpstreamProviderError("Attractions service is temporarily unavailable")

    response = await client.get("/api/v1/destinations/paris-france/attractions")

    assert response.status_code == 502
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "UPSTREAM_PROVIDER_ERROR"


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock, return_value=MOCK_OTM_PLACES)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock, return_value=MOCK_DESTINATION)
async def test_get_attractions_response_fields(mock_dest, mock_otm, client):
    response = await client.get("/api/v1/destinations/paris-france/attractions?limit=1")

    assert response.status_code == 200
    result = response.json()["data"]["attractions"][0]
    expected_fields = {"id", "name", "category", "description", "address", "latitude", "longitude", "image_url", "rating"}
    assert expected_fields == set(result.keys())


@pytest.mark.asyncio
async def test_get_attractions_invalid_limit_too_low(client):
    response = await client.get("/api/v1/destinations/paris-france/attractions?limit=0")
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_attractions_invalid_limit_too_high(client):
    response = await client.get("/api/v1/destinations/paris-france/attractions?limit=50")
    assert response.status_code == 422
