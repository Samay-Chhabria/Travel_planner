import pytest
from unittest.mock import AsyncMock, patch

from app.services.hotel_service import (
    _rate_to_stars,
    _normalize_place,
    get_hotels_for_destination,
)
from app.utils.converters import rate_to_price_level


MOCK_OTM_HOTEL = {
    "xid": "h12345",
    "name": "Grand Hotel Paris",
    "dist": 500.0,
    "rate": 3,
    "kinds": "accomodations",
    "point": {"lon": 2.3376, "lat": 48.8606},
}

MOCK_OTM_BUDGET_HOTEL = {
    "xid": "h67890",
    "name": "Budget Inn",
    "dist": 200.0,
    "rate": 1,
    "kinds": "accomodations",
    "point": {"lon": 2.34, "lat": 48.85},
}

MOCK_OTM_MID_HOTEL = {
    "xid": "h11111",
    "name": "Mid Stay",
    "dist": 300.0,
    "rate": 2,
    "kinds": "accomodations",
    "point": {"lon": 2.35, "lat": 48.86},
}


def test_rate_to_price_level_budget():
    assert rate_to_price_level(0) == "budget"
    assert rate_to_price_level(1) == "budget"


def test_rate_to_price_level_mid():
    assert rate_to_price_level(2) == "mid_range"


def test_rate_to_price_level_luxury():
    assert rate_to_price_level(3) == "luxury"


def test_rate_to_stars_zero():
    assert _rate_to_stars(0) == 0


def test_rate_to_stars_low():
    assert _rate_to_stars(1) == 2


def test_rate_to_stars_mid():
    assert _rate_to_stars(2) == 3


def test_rate_to_stars_high():
    assert _rate_to_stars(3) == 5


def test_normalize_place():
    hotel = _normalize_place(MOCK_OTM_HOTEL)
    assert hotel.id == "h12345"
    assert hotel.name == "Grand Hotel Paris"
    assert hotel.price_level == "luxury"
    assert hotel.star_rating == 5
    assert hotel.latitude == 48.8606
    assert hotel.longitude == 2.3376
    assert hotel.rating == 5.0


def test_normalize_place_budget():
    hotel = _normalize_place(MOCK_OTM_BUDGET_HOTEL)
    assert hotel.name == "Budget Inn"
    assert hotel.price_level == "budget"
    assert hotel.star_rating == 2
    assert hotel.rating == 1.7


def test_normalize_place_mid():
    hotel = _normalize_place(MOCK_OTM_MID_HOTEL)
    assert hotel.price_level == "mid_range"
    assert hotel.star_rating == 3


def test_normalize_place_empty():
    hotel = _normalize_place({})
    assert hotel.id == ""
    assert hotel.name == "Unnamed"
    assert hotel.price_level == "budget"
    assert hotel.star_rating == 0


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_hotels_for_destination(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_HOTEL, MOCK_OTM_BUDGET_HOTEL]

    results = await get_hotels_for_destination("paris-france", limit=10)

    assert len(results) == 2
    assert results[0].name == "Grand Hotel Paris"
    mock_otm.assert_called_once_with(
        lat=48.8566, lon=2.3522, radius=3000, limit=30,
        kinds="accomodations", rate=0,
    )


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_hotels_budget_filter(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_HOTEL, MOCK_OTM_BUDGET_HOTEL, MOCK_OTM_MID_HOTEL]

    results = await get_hotels_for_destination("paris-france", limit=10, budget="budget")

    assert len(results) == 1
    assert results[0].name == "Budget Inn"


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_hotels_luxury_filter(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_HOTEL, MOCK_OTM_BUDGET_HOTEL]

    results = await get_hotels_for_destination("paris-france", limit=10, budget="luxury")

    assert len(results) == 1
    assert results[0].name == "Grand Hotel Paris"


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_hotels_limit(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_HOTEL, MOCK_OTM_BUDGET_HOTEL]

    results = await get_hotels_for_destination("paris-france", limit=1)

    assert len(results) == 1


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock, return_value=[])
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_hotels_empty(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )

    results = await get_hotels_for_destination("paris-france")

    assert results == []


@pytest.mark.asyncio
@patch("app.services.hotel_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.hotel_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_hotels_budget_alias(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_HOTEL, MOCK_OTM_BUDGET_HOTEL]

    results = await get_hotels_for_destination("paris-france", limit=10, budget="low")

    assert len(results) == 1
    assert results[0].name == "Budget Inn"
