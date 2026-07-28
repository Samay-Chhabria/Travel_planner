import pytest
from datetime import date
from unittest.mock import AsyncMock, patch

from app.schemas.trip_plan import TripPlanRequest
from app.services.trip_planner_service import (
    _get_style_template,
    _build_weather_summary,
    _generate_day_plan,
)


def test_get_style_template_culture():
    t = _get_style_template("culture")
    assert "museum" in t["morning"][0].lower()
    assert "notes" in t


def test_get_style_template_unknown():
    t = _get_style_template("unknown_style")
    assert t == _get_style_template("general")


def test_build_weather_summary_none():
    assert "not available" in _build_weather_summary(None)


def test_build_weather_summary_with_data():
    from app.schemas.weather import WeatherData, CurrentWeather, ForecastDay

    weather = WeatherData(
        destination_id="test",
        current=CurrentWeather(temperature_c=20, temperature_f=68, condition="Clear", description="Clear sky"),
        forecast=[
            ForecastDay(date="2026-08-01", max_temp_c=25, min_temp_c=15, condition="Sunny"),
            ForecastDay(date="2026-08-02", max_temp_c=28, min_temp_c=18, condition="Cloudy"),
        ],
    )
    summary = _build_weather_summary(weather)
    assert "Sunny" in summary
    assert "Cloudy" in summary
    assert "C average" in summary


def test_generate_day_plan_arrival():
    from datetime import date
    day = _generate_day_plan(1, date(2026, 8, 1), {}, "Paris", 5)
    assert day.day == 1
    assert day.date == date(2026, 8, 1)
    assert "Arrive" in day.activities[0].description
    assert day.notes != ""


def test_generate_day_plan_departure():
    from datetime import date
    day = _generate_day_plan(5, date(2026, 8, 5), {}, "Paris", 5)
    assert day.day == 5
    assert any("Check out" in a.description or "depart" in a.description.lower() for a in day.activities)


def test_generate_day_plan_middle():
    from datetime import date
    template = _get_style_template("culture")
    day = _generate_day_plan(3, date(2026, 8, 3), template, "Paris", 5)
    assert day.day == 3
    assert len(day.activities) == 3
    assert day.notes != ""


def test_request_validation_end_before_start():
    with pytest.raises(Exception):
        TripPlanRequest(
            destination="Paris",
            start_date=date(2026, 8, 10),
            end_date=date(2026, 8, 1),
        )


def test_request_validation_same_date():
    req = TripPlanRequest(
        destination="Paris",
        start_date=date(2026, 8, 5),
        end_date=date(2026, 8, 5),
    )
    assert req.start_date == req.end_date


@pytest.mark.asyncio
@patch("app.services.trip_planner_service.search_destinations", new_callable=AsyncMock)
async def test_generate_trip_plan(mock_search):
    from app.schemas.destination import Destination

    mock_search.return_value = [Destination(
        id="paris-france", name="Paris", country="France",
        slug="paris-france", latitude=48.8566, longitude=2.3522,
    )]

    req = TripPlanRequest(
        destination="Paris",
        start_date=date(2026, 8, 1),
        end_date=date(2026, 8, 3),
        travel_style="culture",
        budget_level="moderate",
        group_type="couple",
    )

    from app.services.trip_planner_service import generate_trip_plan
    plan = await generate_trip_plan(req)

    assert plan.destination == "Paris"
    assert plan.country == "France"
    assert plan.duration_days == 3
    assert plan.travel_style == "culture"
    assert plan.budget_level == "moderate"
    assert len(plan.days) == 3
    assert plan.days[0].day == 1
    assert plan.days[2].day == 3
    assert plan.id.startswith("plan-")
