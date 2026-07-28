import pytest
from unittest.mock import AsyncMock, patch

from app.services.attraction_service import (
    _primary_category,
    _otm_rate_to_five,
    _normalize_place,
    get_attractions_for_destination,
)


MOCK_OTM_PLACE = {
    "xid": "n12345",
    "name": "Louvre Museum",
    "dist": 500.0,
    "rate": 3,
    "kinds": "museums,cultural",
    "point": {"lon": 2.3376, "lat": 48.8606},
}

MOCK_OTM_PLACE_UNRATED = {
    "xid": "n67890",
    "name": "Small Park",
    "dist": 200.0,
    "rate": 0,
    "kinds": "natural",
    "point": {"lon": 2.34, "lat": 48.85},
}

MOCK_OTM_PLACE_NO_KINDS = {
    "xid": "n99999",
    "name": "Unknown Spot",
    "dist": 100.0,
    "rate": 2,
    "kinds": "",
    "point": {"lon": 2.35, "lat": 48.86},
}


def test_primary_category_museums():
    assert _primary_category("museums,cultural") == "Museum"


def test_primary_category_monuments():
    assert _primary_category("monuments") == "Monument"


def test_primary_category_natural():
    assert _primary_category("natural,geological_formations") == "Nature"


def test_primary_category_unknown():
    assert _primary_category("custom_kind") == "Custom_Kind"


def test_primary_category_empty():
    assert _primary_category("") == ""


def test_otm_rate_to_five_max():
    assert _otm_rate_to_five(3) == 5.0


def test_otm_rate_to_five_mid():
    assert _otm_rate_to_five(2) == 3.3


def test_otm_rate_to_five_low():
    assert _otm_rate_to_five(1) == 1.7


def test_otm_rate_to_five_zero():
    assert _otm_rate_to_five(0) == 0.0


def test_normalize_place():
    attraction = _normalize_place(MOCK_OTM_PLACE)
    assert attraction.id == "n12345"
    assert attraction.name == "Louvre Museum"
    assert attraction.category == "Museum"
    assert attraction.latitude == 48.8606
    assert attraction.longitude == 2.3376
    assert attraction.rating == 5.0


def test_normalize_place_unrated():
    attraction = _normalize_place(MOCK_OTM_PLACE_UNRATED)
    assert attraction.name == "Small Park"
    assert attraction.category == "Nature"
    assert attraction.rating == 0.0


def test_normalize_place_no_kinds():
    attraction = _normalize_place(MOCK_OTM_PLACE_NO_KINDS)
    assert attraction.category == ""


def test_normalize_place_empty():
    attraction = _normalize_place({})
    assert attraction.id == ""
    assert attraction.name == "Unnamed"
    assert attraction.latitude == 0.0


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_attractions_for_destination(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_PLACE, MOCK_OTM_PLACE_UNRATED]

    results = await get_attractions_for_destination("paris-france", limit=10)

    assert len(results) == 2
    assert results[0].name == "Louvre Museum"
    mock_otm.assert_called_once_with(
        lat=48.8566, lon=2.3522, radius=2000, limit=20, rate=1,
    )


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_attractions_with_category_filter(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_PLACE, MOCK_OTM_PLACE_UNRATED]

    results = await get_attractions_for_destination("paris-france", limit=10, category="Museum")

    assert len(results) == 1
    assert results[0].name == "Louvre Museum"


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock)
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_attractions_limit(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )
    mock_otm.return_value = [MOCK_OTM_PLACE, MOCK_OTM_PLACE_UNRATED]

    results = await get_attractions_for_destination("paris-france", limit=1)

    assert len(results) == 1


@pytest.mark.asyncio
@patch("app.services.attraction_service.get_nearby_places", new_callable=AsyncMock, return_value=[])
@patch("app.services.attraction_service.get_destination_by_id", new_callable=AsyncMock)
async def test_get_attractions_empty(mock_dest, mock_otm):
    from app.schemas.destination import Destination

    mock_dest.return_value = Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )

    results = await get_attractions_for_destination("paris-france")

    assert results == []
