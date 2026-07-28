from app.services.weather_service import (
    _normalize_current,
    _normalize_forecast,
    _celsius_to_fahrenheit,
)
from app.integrations.providers.open_meteo_client import decode_weather_code, WMO_WEATHER_CODES


def test_decode_known_weather_code():
    result = decode_weather_code(0)
    assert result["condition"] == "Clear"
    assert result["description"] == "Clear sky"


def test_decode_unknown_weather_code():
    result = decode_weather_code(9999)
    assert result["condition"] == "Unknown"


def test_all_wmo_codes_have_valid_format():
    for code, info in WMO_WEATHER_CODES.items():
        assert "condition" in info
        assert "description" in info
        assert isinstance(info["condition"], str)
        assert isinstance(info["description"], str)


def test_celsius_to_fahrenheit():
    assert _celsius_to_fahrenheit(0) == 32.0
    assert _celsius_to_fahrenheit(100) == 212.0
    assert _celsius_to_fahrenheit(20) == 68.0


def test_normalize_current():
    raw = {
        "temperature_2m": 22.5,
        "weather_code": 1,
        "relative_humidity_2m": 65,
        "wind_speed_10m": 12.3,
    }
    result = _normalize_current(raw)
    assert result.temperature_c == 22.5
    assert result.temperature_f == 72.5
    assert result.condition == "Mostly Clear"
    assert result.description == "Mainly clear"


def test_normalize_current_clear_sky():
    raw = {"temperature_2m": 15.0, "weather_code": 0}
    result = _normalize_current(raw)
    assert result.condition == "Clear"
    assert result.temperature_c == 15.0
    assert result.temperature_f == 59.0


def test_normalize_forecast():
    raw_daily = {
        "time": ["2026-07-13", "2026-07-14"],
        "temperature_2m_max": [30.0, 28.5],
        "temperature_2m_min": [18.0, 16.5],
        "weather_code": [0, 61],
    }
    result = _normalize_forecast(raw_daily)
    assert len(result) == 2
    assert result[0].date == "2026-07-13"
    assert result[0].max_temp_c == 30.0
    assert result[0].min_temp_c == 18.0
    assert result[0].condition == "Clear"
    assert result[1].condition == "Rain"


def test_normalize_forecast_empty():
    raw_daily = {"time": [], "temperature_2m_max": [], "temperature_2m_min": [], "weather_code": []}
    result = _normalize_forecast(raw_daily)
    assert result == []


def test_normalize_forecast_missing_keys():
    raw_daily = {}
    result = _normalize_forecast(raw_daily)
    assert result == []
