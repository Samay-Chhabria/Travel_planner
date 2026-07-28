import pytest

from app.integrations.providers.nominatim_client import _normalize_place
from app.services.geocoding_service import _to_geocoding_result, _build_cache_key


MOCK_NOMINATIM_RAW = {
    "place_id": 97683695,
    "lat": "48.8534951",
    "lon": "2.3483915",
    "name": "Paris",
    "display_name": "Paris, Ile-de-France, Metropolitan France, France",
    "type": "administrative",
    "importance": 0.897,
    "address": {
        "city": "Paris",
        "state": "Ile-de-France",
        "country": "France",
        "country_code": "fr",
    },
}

MOCK_NOMINATIM_RAW_NO_ADDRESS = {
    "place_id": 12345,
    "lat": "51.5074",
    "lon": "-0.1278",
    "name": "London",
    "display_name": "London, England, United Kingdom",
    "type": "city",
    "importance": 0.9,
    "address": {},
}


def test_normalize_place():
    result = _normalize_place(MOCK_NOMINATIM_RAW)
    assert result["place_id"] == "97683695"
    assert result["name"] == "Paris"
    assert result["latitude"] == 48.8534951
    assert result["longitude"] == 2.3483915
    assert result["country"] == "France"
    assert result["country_code"] == "fr"
    assert result["region"] == "Ile-de-France"
    assert result["city"] == "Paris"
    assert result["place_type"] == "administrative"
    assert result["importance"] == 0.897


def test_normalize_place_empty_address():
    result = _normalize_place(MOCK_NOMINATIM_RAW_NO_ADDRESS)
    assert result["name"] == "London"
    assert result["country"] == ""
    assert result["country_code"] == ""
    assert result["region"] == ""
    assert result["city"] == ""


def test_to_geocoding_result():
    raw = _normalize_place(MOCK_NOMINATIM_RAW)
    result = _to_geocoding_result(raw)
    assert result.id == "97683695"
    assert result.name == "Paris"
    assert result.latitude == 48.8534951
    assert result.longitude == 2.3483915
    assert result.country == "France"
    assert result.display_name == "Paris, Ile-de-France, Metropolitan France, France"


def test_build_cache_key():
    assert _build_cache_key("paris", 10, None) == "paris:10:"
    assert _build_cache_key("paris", 5, "fr") == "paris:5:fr"
    assert _build_cache_key("london", 10, "GB") == "london:10:GB"
