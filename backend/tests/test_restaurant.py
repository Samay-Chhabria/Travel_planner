import pytest
from unittest.mock import AsyncMock, patch

from app.services.restaurant_service import (
    _extract_cuisine,
    _normalize_place,
    get_restaurants_for_destination,
)
from app.utils.converters import rate_to_price_level


MOCK_OTM_RESTAURANT = {
    "xid": "r12345",
    "name": "Le Petit Bistro",
    "dist": 400.0,
    "rate": 3,
    "kinds": "foods,restaurants",
    "point": {"lon": 2.3376, "lat": 48.8606},
}

MOCK_OTM_CAFE = {
    "xid": "r67890",
    "name": "Corner Cafe",
    "dist": 200.0,
    "rate": 1,
    "kinds": "foods",
    "point": {"lon": 2.34, "lat": 48.85},
}

MOCK_OTM_FOODSTALL = {
    "xid": "r11111",
    "name": "Tokyo Ramen Stand",
    "dist": 300.0,
    "rate": 2,
    "kinds": "foods,restaurants",
    "point": {"lon": 2.35, "lat": 48.86},
}


def test_rate_to_price_level_budget():
    assert rate_to_price_level(0) == "budget"
    assert rate_to_price_level(1) == "budget"


def test_rate_to_price_level_mid():
    assert rate_to_price_level(2) == "mid_range"


def test_rate_to_price_level_luxury():
    assert rate_to_price_level(3) == "luxury"


def test_extract_cuisine_with_restaurants():
    assert _extract_cuisine("foods,restaurants") == "Restaurants"


def test_extract_cuisine_foods_only():
    assert _extract_cuisine("foods") == ""


def test_extract_cuisine_empty():
    assert _extract_cuisine("") == ""


def test_normalize_place():
    restaurant = _normalize_place(MOCK_OTM_RESTAURANT)
    assert restaurant.id == "r12345"
    assert restaurant.name == "Le Petit Bistro"
    assert restaurant.price_level == "luxury"
    assert restaurant.latitude == 48.8606
    assert restaurant.longitude == 2.3376
    assert restaurant.rating == 5.0


def test_normalize_place_budget():
    restaurant = _normalize_place(MOCK_OTM_CAFE)
    assert restaurant.name == "Corner Cafe"
    assert restaurant.price_level == "budget"
    assert restaurant.rating == 1.7


def test_normalize_place_mid():
    restaurant = _normalize_place(MOCK_OTM_FOODSTALL)
    assert restaurant.price_level == "mid_range"


def test_normalize_place_empty():
    restaurant = _normalize_place({})
    assert restaurant.id == ""
    assert restaurant.name == "Unnamed"
    assert restaurant.price_level == "budget"


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_restaurants_for_destination(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_RESTAURANT, MOCK_OTM_CAFE]

    results = await get_restaurants_for_destination("paris-france", limit=10)

    assert len(results) == 2
    assert results[0].name == "Le Petit Bistro"
    mock_otm.assert_called_once_with(
        lat=48.8566, lon=2.3522, radius=2000, limit=30,
        kinds="foods", rate=0,
    )


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_restaurants_cuisine_filter(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_RESTAURANT, MOCK_OTM_CAFE]

    results = await get_restaurants_for_destination("paris-france", limit=10, cuisine="bistro")

    assert len(results) == 1
    assert results[0].name == "Le Petit Bistro"


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_restaurants_limit(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_RESTAURANT, MOCK_OTM_CAFE]

    results = await get_restaurants_for_destination("paris-france", limit=1)

    assert len(results) == 1


@pytest.mark.asyncio
@patch("app.services.restaurant_service.get_nearby_places", new_callable=AsyncMock, return_value=[])
@patch("app.services.restaurant_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_restaurants_empty(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )

    results = await get_restaurants_for_destination("paris-france")

    assert results == []
