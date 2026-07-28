import pytest
from unittest.mock import patch, AsyncMock

from app.services import geocoding_service


MOCK_SEARCH_RESULTS = [
    {
        "place_id": "97683695",
        "name": "Paris",
        "display_name": "Paris, Ile-de-France, Metropolitan France, France",
        "latitude": 48.8534951,
        "longitude": 2.3483915,
        "country": "France",
        "country_code": "fr",
        "region": "Ile-de-France",
        "city": "Paris",
        "place_type": "administrative",
        "importance": 0.897,
    },
    {
        "place_id": "333846024",
        "name": "Paris",
        "display_name": "Paris, Lamar County, Texas, United States",
        "latitude": 33.6617962,
        "longitude": -95.555513,
        "country": "United States",
        "country_code": "us",
        "region": "Texas",
        "city": "Paris",
        "place_type": "town",
        "importance": 0.53,
    },
]


@pytest.fixture(autouse=True)
def _clear_geocode_cache():
    geocoding_service._search_cache.clear()
    yield
    geocoding_service._search_cache.clear()


@pytest.mark.asyncio
@patch("app.services.geocoding_service.search_places", new_callable=AsyncMock, return_value=MOCK_SEARCH_RESULTS)
async def test_search_success(mock_search, client):
    response = await client.get("/api/v1/geocoding/search?q=paris")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Locations retrieved successfully"

    data = body["data"]
    assert len(data["results"]) == 2
    assert data["results"][0]["name"] == "Paris"
    assert data["results"][0]["country"] == "France"
    assert data["results"][1]["country"] == "United States"
    assert data["pagination"]["total"] == 2
    assert data["pagination"]["page"] == 1


@pytest.mark.asyncio
@patch("app.services.geocoding_service.search_places", new_callable=AsyncMock, return_value=MOCK_SEARCH_RESULTS)
async def test_search_with_limit(mock_search, client):
    response = await client.get("/api/v1/geocoding/search?q=paris&limit=1")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["results"]) == 1
    assert body["data"]["pagination"]["total"] == 2
    assert body["data"]["pagination"]["limit"] == 1


@pytest.mark.asyncio
@patch("app.services.geocoding_service.search_places", new_callable=AsyncMock, return_value=MOCK_SEARCH_RESULTS)
async def test_search_with_country_filter(mock_search, client):
    response = await client.get("/api/v1/geocoding/search?q=paris&country=fr")

    assert response.status_code == 200
    mock_search.assert_called_once_with(query="paris", limit=25, country_code="fr")


@pytest.mark.asyncio
@patch("app.services.geocoding_service.search_places", new_callable=AsyncMock, return_value=MOCK_SEARCH_RESULTS)
async def test_search_pagination(mock_search, client):
    response = await client.get("/api/v1/geocoding/search?q=paris&limit=1&page=2")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["results"]) == 1
    assert body["data"]["results"][0]["country"] == "United States"
    assert body["data"]["pagination"]["page"] == 2


@pytest.mark.asyncio
@patch("app.services.geocoding_service.search_places", new_callable=AsyncMock, return_value=[])
async def test_search_no_results(mock_search, client):
    response = await client.get("/api/v1/geocoding/search?q=xyznonexistent")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["results"] == []
    assert body["data"]["pagination"]["total"] == 0


async def test_search_query_too_short(client):
    response = await client.get("/api/v1/geocoding/search?q=a")
    assert response.status_code == 422


async def test_search_missing_query(client):
    response = await client.get("/api/v1/geocoding/search")
    assert response.status_code == 422


@pytest.mark.asyncio
@patch("app.services.geocoding_service.search_places", new_callable=AsyncMock)
async def test_search_upstream_failure(mock_search, client):
    from app.core.exceptions import UpstreamProviderError

    mock_search.side_effect = UpstreamProviderError("Geocoding service is temporarily unavailable")

    response = await client.get("/api/v1/geocoding/search?q=paris")

    assert response.status_code == 502
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "UPSTREAM_PROVIDER_ERROR"


@pytest.mark.asyncio
@patch("app.services.geocoding_service.search_places", new_callable=AsyncMock, return_value=MOCK_SEARCH_RESULTS)
async def test_search_response_model_fields(mock_search, client):
    response = await client.get("/api/v1/geocoding/search?q=paris&limit=1")

    assert response.status_code == 200
    result = response.json()["data"]["results"][0]
    expected_fields = {"id", "name", "display_name", "latitude", "longitude", "country", "country_code", "region", "city", "place_type", "importance"}
    assert expected_fields == set(result.keys())


@pytest.mark.asyncio
@patch("app.services.geocoding_service.search_places", new_callable=AsyncMock, return_value=MOCK_SEARCH_RESULTS)
async def test_search_query_echoed(mock_search, client):
    response = await client.get("/api/v1/geocoding/search?q=paris")

    assert response.status_code == 200
    assert response.json()["data"]["query"] == "paris"
