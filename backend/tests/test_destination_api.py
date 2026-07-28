import pytest
from unittest.mock import patch, AsyncMock

from app.schemas.geocoding import GeocodingResult


MOCK_GEOCODING_RESULTS = [
    GeocodingResult(
        id="97683695",
        name="Paris",
        display_name="Paris, Ile-de-France, Metropolitan France, France",
        latitude=48.8534951,
        longitude=2.3483915,
        country="France",
        country_code="fr",
        region="Ile-de-France",
        city="Paris",
        place_type="administrative",
        importance=0.897,
    ),
    GeocodingResult(
        id="333846024",
        name="Paris",
        display_name="Paris, Lamar County, Texas, United States",
        latitude=33.6617962,
        longitude=-95.555513,
        country="United States",
        country_code="us",
        region="Texas",
        city="Paris",
        place_type="town",
        importance=0.53,
    ),
]


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock, return_value=MOCK_GEOCODING_RESULTS)
async def test_search_success(mock_search, client):
    response = await client.get("/api/v1/destinations/search?q=paris")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Destinations retrieved successfully"

    data = body["data"]
    assert len(data["results"]) == 1
    assert data["results"][0]["name"] == "Paris"
    assert data["results"][0]["country"] == "France"
    assert data["pagination"]["total"] == 1
    assert data["pagination"]["page"] == 1


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock, return_value=MOCK_GEOCODING_RESULTS)
async def test_search_with_limit(mock_search, client):
    response = await client.get("/api/v1/destinations/search?q=paris&limit=1")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["results"]) == 1
    assert body["data"]["pagination"]["total"] == 1
    assert body["data"]["pagination"]["limit"] == 1


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock, return_value=MOCK_GEOCODING_RESULTS)
async def test_search_with_country_filter(mock_search, client):
    response = await client.get("/api/v1/destinations/search?q=paris&country=fr")

    assert response.status_code == 200
    mock_search.assert_called_once_with(query="paris", limit=25, country_code="fr")


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock, return_value=MOCK_GEOCODING_RESULTS)
async def test_search_pagination(mock_search, client):
    response = await client.get("/api/v1/destinations/search?q=paris&limit=1&page=2")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["results"]) == 0
    assert body["data"]["pagination"]["page"] == 2
    assert body["data"]["pagination"]["total"] == 1


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock, return_value=[])
async def test_search_no_results(mock_search, client):
    response = await client.get("/api/v1/destinations/search?q=xyznonexistent")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["results"] == []
    assert body["data"]["pagination"]["total"] == 0


async def test_search_query_too_short(client):
    response = await client.get("/api/v1/destinations/search?q=a")
    assert response.status_code == 422


async def test_search_missing_query(client):
    response = await client.get("/api/v1/destinations/search")
    assert response.status_code == 422


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock, return_value=MOCK_GEOCODING_RESULTS)
async def test_search_response_model_fields(mock_search, client):
    response = await client.get("/api/v1/destinations/search?q=paris&limit=1")

    assert response.status_code == 200
    result = response.json()["data"]["results"][0]
    expected_fields = {
        "id", "name", "country", "region", "slug", "latitude", "longitude",
        "description", "image_url", "highlights", "best_time_to_visit", "travel_type",
    }
    assert expected_fields == set(result.keys())


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock, return_value=MOCK_GEOCODING_RESULTS)
async def test_search_query_echoed(mock_search, client):
    response = await client.get("/api/v1/destinations/search?q=paris")

    assert response.status_code == 200
    assert response.json()["data"]["query"] == "paris"


@pytest.mark.asyncio
async def test_featured_success(client):
    response = await client.get("/api/v1/destinations/featured")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Featured destinations retrieved successfully"
    assert len(body["data"]["destinations"]) == 6


@pytest.mark.asyncio
async def test_featured_with_limit(client):
    response = await client.get("/api/v1/destinations/featured?limit=2")

    assert response.status_code == 200
    body = response.json()
    assert len(body["data"]["destinations"]) == 2


@pytest.mark.asyncio
async def test_detail_featured_destination(client):
    response = await client.get("/api/v1/destinations/paris-france")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["destination"]["id"] == "paris-france"
    assert body["data"]["destination"]["name"] == "Paris"


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock)
async def test_detail_geocode_fallback(mock_search, client):
    mock_search.return_value = [MOCK_GEOCODING_RESULTS[0]]
    response = await client.get("/api/v1/destinations/unknown-place")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["destination"]["name"] == "Paris"
    mock_search.assert_called_once_with(query="unknown place", limit=1)


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock)
async def test_detail_geocode_multi_word_country(mock_search, client):
    mock_search.return_value = [GeocodingResult(
        id="12345", name="Queenstown", display_name="Queenstown, Otago, New Zealand",
        latitude=-45.0312, longitude=168.6626, country="New Zealand",
        country_code="nz", region="Otago", city="Queenstown",
        place_type="town", importance=0.6,
    )]
    response = await client.get("/api/v1/destinations/queenstown-new-zealand")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["data"]["destination"]["name"] == "Queenstown"
    assert body["data"]["destination"]["country"] == "New Zealand"
    mock_search.assert_called_once_with(query="queenstown new zealand", limit=1)


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock, return_value=[])
async def test_detail_not_found(mock_search, client):
    response = await client.get("/api/v1/destinations/nonexistent-place")

    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "NOT_FOUND"


@pytest.mark.asyncio
async def test_detail_london_returns_complete_data(client):
    response = await client.get("/api/v1/destinations/london-united-kingdom")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True

    dest = body["data"]["destination"]
    assert dest["id"] == "london-united-kingdom"
    assert dest["name"] == "London"
    assert dest["country"] == "United Kingdom"
    assert dest["region"] == "England"
    assert dest["slug"] == "london-united-kingdom"
    assert isinstance(dest["latitude"], float)
    assert isinstance(dest["longitude"], float)
    assert dest["latitude"] == 51.5074
    assert dest["longitude"] == -0.1278
    assert dest["description"] != ""
    assert dest["description"] != "Explore London, United Kingdom"
    assert dest["image_url"] != ""
    assert len(dest["highlights"]) > 0
    assert dest["best_time_to_visit"] != ""
    assert dest["travel_type"] == "City"


@pytest.mark.asyncio
async def test_detail_karachi_returns_complete_data(client):
    response = await client.get("/api/v1/destinations/karachi-pakistan")

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True

    dest = body["data"]["destination"]
    assert dest["id"] == "karachi-pakistan"
    assert dest["name"] == "Karachi"
    assert dest["country"] == "Pakistan"
    assert dest["region"] == "Sindh"
    assert dest["slug"] == "karachi-pakistan"
    assert isinstance(dest["latitude"], float)
    assert isinstance(dest["longitude"], float)
    assert dest["latitude"] == 24.8607
    assert dest["longitude"] == 67.0011
    assert dest["description"] != ""
    assert dest["description"] != "Explore Karachi, Pakistan"
    assert dest["image_url"] != ""
    assert len(dest["highlights"]) > 0
    assert dest["best_time_to_visit"] != ""
    assert dest["travel_type"] == "City"


@pytest.mark.asyncio
async def test_detail_paris_returns_complete_data(client):
    response = await client.get("/api/v1/destinations/paris-france")

    assert response.status_code == 200
    body = response.json()
    dest = body["data"]["destination"]
    assert dest["id"] == "paris-france"
    assert dest["name"] == "Paris"
    assert dest["country"] == "France"
    assert dest["latitude"] == 48.8566
    assert dest["longitude"] == 2.3522
    assert dest["description"] != ""
    assert dest["image_url"] != ""
    assert len(dest["highlights"]) > 0
    assert dest["best_time_to_visit"] != ""
    assert dest["travel_type"] == "City"


@pytest.mark.asyncio
async def test_detail_tokyo_returns_complete_data(client):
    response = await client.get("/api/v1/destinations/tokyo-japan")

    assert response.status_code == 200
    body = response.json()
    dest = body["data"]["destination"]
    assert dest["id"] == "tokyo-japan"
    assert dest["name"] == "Tokyo"
    assert dest["country"] == "Japan"
    assert dest["latitude"] == 35.6762
    assert dest["longitude"] == 139.6503
    assert dest["description"] != ""
    assert dest["image_url"] != ""
    assert len(dest["highlights"]) > 0
    assert dest["best_time_to_visit"] != ""
    assert dest["travel_type"] == "City"
