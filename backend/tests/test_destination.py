import pytest
from unittest.mock import AsyncMock, patch

from app.schemas.geocoding import GeocodingResult
from app.schemas.destination import Destination
from app.services.destination_service import (
    _make_slug,
    _infer_travel_type,
    _geocode_to_destination,
    _deduplicate_by_name,
    _DESTINATION_IMAGE_MAP,
    _FEATURED_DESTINATIONS,
    DEFAULT_DESTINATION_IMAGE,
    get_featured_destinations,
    get_destination_by_id,
    search_destinations,
)


MOCK_GEOCODING_RESULT = GeocodingResult(
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
)


def test_make_slug():
    assert _make_slug("Paris", "France") == "paris-france"
    assert _make_slug("New York", "United States") == "new-york-united-states"
    assert _make_slug("Tokyo", "Japan") == "tokyo-japan"


def test_infer_travel_type_city():
    assert _infer_travel_type("city", "London") == "City"
    assert _infer_travel_type("administrative", "Paris") == "City"
    assert _infer_travel_type("town", "Austin") == "City"


def test_infer_travel_type_rural():
    assert _infer_travel_type("village", "Cotswold") == "Rural"
    assert _infer_travel_type("hamlet", "Smallville") == "Rural"


def test_infer_travel_type_beach():
    assert _infer_travel_type("island", "Maui") == "Beach"
    assert _infer_travel_type("locality", "Bondi Beach") == "Beach"


def test_infer_travel_type_adventure():
    assert _infer_travel_type("mountain", "Everest") == "Adventure"


def test_geocode_to_destination():
    dest = _geocode_to_destination(MOCK_GEOCODING_RESULT)
    assert dest.id == "paris-france"
    assert dest.name == "Paris"
    assert dest.country == "France"
    assert dest.region == "Ile-de-France"
    assert dest.slug == "paris-france"
    assert dest.latitude == 48.8534951
    assert dest.longitude == 2.3483915
    assert dest.travel_type == "City"
    assert len(dest.highlights) > 0
    assert dest.best_time_to_visit != ""
    assert dest.description != f"Explore {dest.name}, {dest.country}"
    assert dest.image_url == _DESTINATION_IMAGE_MAP["paris"]


def test_geocode_to_destination_unknown_place():
    unknown = GeocodingResult(
        id="99999999", name="Randomville", display_name="Randomville, Nowhere",
        latitude=10.0, longitude=20.0, country="Nowhere",
        country_code="nw", region="Nowhere Region", city="Randomville",
        place_type="town", importance=0.4,
    )
    dest = _geocode_to_destination(unknown)
    assert dest.image_url == DEFAULT_DESTINATION_IMAGE


def test_geocode_to_destination_known_places_get_unique_images():
    places = [
        GeocodingResult(
            id="1", name="Paris", display_name="Paris, France",
            latitude=48.85, longitude=2.34, country="France",
            country_code="fr", region="Ile-de-France", city="Paris",
            place_type="administrative", importance=0.897,
        ),
        GeocodingResult(
            id="2", name="Tokyo", display_name="Tokyo, Japan",
            latitude=35.68, longitude=139.69, country="Japan",
            country_code="jp", region="Kanto", city="Tokyo",
            place_type="city", importance=0.95,
        ),
        GeocodingResult(
            id="3", name="London", display_name="London, UK",
            latitude=51.5, longitude=-0.12, country="United Kingdom",
            country_code="gb", region="England", city="London",
            place_type="city", importance=0.92,
        ),
    ]
    images = [_geocode_to_destination(p).image_url for p in places]
    assert len(set(images)) == 3
    for img in images:
        assert img != DEFAULT_DESTINATION_IMAGE


def test_destination_image_map_covers_featured_destinations():
    for dest in _FEATURED_DESTINATIONS:
        key = dest.name.lower().strip()
        assert key in _DESTINATION_IMAGE_MAP, f"Missing image map entry for {dest.name}"
        assert _DESTINATION_IMAGE_MAP[key] == dest.image_url


def test_deduplicate_by_name_keeps_highest_importance():
    low = GeocodingResult(
        id="1", name="Paris", display_name="Paris, Texas, US",
        latitude=33.66, longitude=-95.55, country="United States",
        country_code="us", region="Texas", city="Paris",
        place_type="town", importance=0.53,
    )
    high = GeocodingResult(
        id="2", name="Paris", display_name="Paris, Ile-de-France, France",
        latitude=48.85, longitude=2.34, country="France",
        country_code="fr", region="Ile-de-France", city="Paris",
        place_type="administrative", importance=0.897,
    )
    result = _deduplicate_by_name([low, high])
    assert len(result) == 1
    assert result[0].id == "2"
    assert result[0].importance == 0.897


def test_deduplicate_by_name_preserves_unique_names():
    a = GeocodingResult(
        id="1", name="Paris", display_name="Paris, France",
        latitude=48.85, longitude=2.34, country="France",
        country_code="fr", region="Ile-de-France", city="Paris",
        place_type="administrative", importance=0.897,
    )
    b = GeocodingResult(
        id="2", name="London", display_name="London, UK",
        latitude=51.5, longitude=-0.12, country="United Kingdom",
        country_code="gb", region="England", city="London",
        place_type="city", importance=0.9,
    )
    result = _deduplicate_by_name([a, b])
    assert len(result) == 2


def test_get_featured_destinations_default():
    featured = get_featured_destinations()
    assert len(featured) == 6
    assert featured[0].id == "paris-france"
    assert featured[1].id == "tokyo-japan"
    assert featured[2].id == "bali-indonesia"
    assert featured[3].id == "santorini-greece"
    assert featured[4].id == "new-york-usa"
    assert featured[5].id == "cape-town-south-africa"


def test_get_featured_destinations_all():
    featured = get_featured_destinations(limit=100)
    assert len(featured) == 8
    assert featured[6].id == "london-united-kingdom"
    assert featured[7].id == "karachi-pakistan"


def test_get_featured_destinations_limit():
    featured = get_featured_destinations(limit=2)
    assert len(featured) == 2


def test_get_featured_destinations_limit_exceeds():
    featured = get_featured_destinations(limit=100)
    assert len(featured) == len(_FEATURED_DESTINATIONS)
    assert len(featured) == 8


@pytest.mark.asyncio
async def test_get_destination_by_id_featured():
    dest = await get_destination_by_id("paris-france")
    assert dest.id == "paris-france"
    assert dest.name == "Paris"


@pytest.mark.asyncio
async def test_get_destination_by_id_slug_match():
    dest = await get_destination_by_id("tokyo-japan")
    assert dest.id == "tokyo-japan"


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock)
async def test_get_destination_by_id_geocode_fallback(mock_search):
    mock_search.return_value = [MOCK_GEOCODING_RESULT]
    dest = await get_destination_by_id("paris-france-fallback")
    assert dest.name == "Paris"
    mock_search.assert_called_once_with(query="paris france fallback", limit=1)


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock)
async def test_get_destination_by_id_geocode_multi_word_country(mock_search):
    mock_search.return_value = [GeocodingResult(
        id="12345", name="Queenstown", display_name="Queenstown, Otago, New Zealand",
        latitude=-45.0312, longitude=168.6626, country="New Zealand",
        country_code="nz", region="Otago", city="Queenstown",
        place_type="town", importance=0.6,
    )]
    dest = await get_destination_by_id("queenstown-new-zealand")
    assert dest.name == "Queenstown"
    assert dest.country == "New Zealand"
    mock_search.assert_called_once_with(query="queenstown new zealand", limit=1)


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock)
async def test_get_destination_by_id_not_found(mock_search):
    mock_search.return_value = []
    from app.core.exceptions import NotFoundError
    with pytest.raises(NotFoundError):
        await get_destination_by_id("nonexistent-place")


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock)
async def test_search_destinations(mock_search):
    mock_search.return_value = [MOCK_GEOCODING_RESULT]
    results = await search_destinations(query="paris", limit=10)
    assert len(results) == 1
    assert results[0].name == "Paris"
    assert results[0].country == "France"
    mock_search.assert_called_once_with(query="paris", limit=10, country_code=None)


@pytest.mark.asyncio
@patch("app.services.destination_service.search_locations", new_callable=AsyncMock)
async def test_search_destinations_empty(mock_search):
    mock_search.return_value = []
    results = await search_destinations(query="xyznonexistent")
    assert results == []
