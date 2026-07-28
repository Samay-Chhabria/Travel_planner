import pytest
from datetime import date
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


@pytest.mark.asyncio
@patch("app.services.trip_planner_service._safe_fetch", new_callable=AsyncMock, return_value=[])
@patch("app.services.trip_planner_service.search_destinations", new_callable=AsyncMock, return_value=[MOCK_DESTINATION])
async def test_generate_plan_success(mock_search, mock_fetch, client):
    response = await client.post("/api/v1/trip-planner/generate", json={
        "destination": "Paris",
        "start_date": "2026-08-01",
        "end_date": "2026-08-03",
        "travel_style": "culture",
        "budget_level": "moderate",
        "group_type": "couple",
    })

    assert response.status_code == 200
    body = response.json()
    assert body["success"] is True
    assert body["message"] == "Trip plan generated successfully"

    plan = body["data"]["plan"]
    assert plan["destination"] == "Paris"
    assert plan["country"] == "France"
    assert plan["duration_days"] == 3
    assert plan["travel_style"] == "culture"
    assert plan["budget_level"] == "moderate"
    assert plan["group_type"] == "couple"
    assert len(plan["days"]) == 3
    assert plan["id"].startswith("plan-")
    assert plan["summary"] != ""


@pytest.mark.asyncio
@patch("app.services.trip_planner_service._safe_fetch", new_callable=AsyncMock, return_value=[])
@patch("app.services.trip_planner_service.search_destinations", new_callable=AsyncMock, return_value=[MOCK_DESTINATION])
async def test_generate_plan_single_day(mock_search, mock_fetch, client):
    response = await client.post("/api/v1/trip-planner/generate", json={
        "destination": "Paris",
        "start_date": "2026-08-01",
        "end_date": "2026-08-01",
    })

    assert response.status_code == 200
    body = response.json()
    assert body["data"]["plan"]["duration_days"] == 1
    assert len(body["data"]["plan"]["days"]) == 1


@pytest.mark.asyncio
@patch("app.services.trip_planner_service._safe_fetch", new_callable=AsyncMock, return_value=[])
@patch("app.services.trip_planner_service.search_destinations", new_callable=AsyncMock, return_value=[MOCK_DESTINATION])
async def test_generate_plan_all_styles(mock_search, mock_fetch, client):
    for style in ("culture", "adventure", "food", "relaxation", "general"):
        response = await client.post("/api/v1/trip-planner/generate", json={
            "destination": "Paris",
            "start_date": "2026-08-01",
            "end_date": "2026-08-02",
            "travel_style": style,
        })
        assert response.status_code == 200
        assert response.json()["data"]["plan"]["travel_style"] == style


@pytest.mark.asyncio
@patch("app.services.trip_planner_service._safe_fetch", new_callable=AsyncMock, return_value=[])
@patch("app.services.trip_planner_service.search_destinations", new_callable=AsyncMock, return_value=[MOCK_DESTINATION])
async def test_generate_plan_day_titles(mock_search, mock_fetch, client):
    response = await client.post("/api/v1/trip-planner/generate", json={
        "destination": "Paris",
        "start_date": "2026-08-01",
        "end_date": "2026-08-05",
    })

    assert response.status_code == 200
    days = response.json()["data"]["plan"]["days"]
    assert len(days) == 5
    assert "First Impressions" in days[0]["title"]
    assert "Farewell" in days[-1]["title"]


@pytest.mark.asyncio
@patch("app.services.trip_planner_service._safe_fetch", new_callable=AsyncMock, return_value=[])
@patch("app.services.trip_planner_service.search_destinations", new_callable=AsyncMock, return_value=[MOCK_DESTINATION])
async def test_generate_plan_fields(mock_search, mock_fetch, client):
    response = await client.post("/api/v1/trip-planner/generate", json={
        "destination": "Paris",
        "start_date": "2026-08-01",
        "end_date": "2026-08-02",
    })

    assert response.status_code == 200
    plan = response.json()["data"]["plan"]
    expected_fields = {
        "id", "destination", "country", "duration_days", "travel_style",
        "budget_level", "group_type", "summary", "days", "weather_summary",
        "top_attractions", "recommended_hotels", "recommended_restaurants",
    }
    assert expected_fields == set(plan.keys())


@pytest.mark.asyncio
async def test_generate_plan_missing_destination(client):
    response = await client.post("/api/v1/trip-planner/generate", json={
        "start_date": "2026-08-01",
        "end_date": "2026-08-03",
    })
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_generate_plan_empty_destination(client):
    response = await client.post("/api/v1/trip-planner/generate", json={
        "destination": "",
        "start_date": "2026-08-01",
        "end_date": "2026-08-03",
    })
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_generate_plan_missing_dates(client):
    response = await client.post("/api/v1/trip-planner/generate", json={
        "destination": "Paris",
    })
    assert response.status_code == 422


@pytest.mark.asyncio
async def test_generate_plan_end_before_start(client):
    response = await client.post("/api/v1/trip-planner/generate", json={
        "destination": "Paris",
        "start_date": "2026-08-10",
        "end_date": "2026-08-01",
    })
    assert response.status_code == 422


@pytest.mark.asyncio
@patch("app.services.trip_planner_service._safe_fetch", new_callable=AsyncMock, return_value=[])
@patch("app.services.trip_planner_service.search_destinations", new_callable=AsyncMock, return_value=[])
async def test_generate_plan_destination_not_found(mock_search, mock_fetch, client):
    response = await client.post("/api/v1/trip-planner/generate", json={
        "destination": "Nonexistent Place",
        "start_date": "2026-08-01",
        "end_date": "2026-08-03",
    })

    assert response.status_code == 404
    body = response.json()
    assert body["success"] is False
    assert body["error"]["code"] == "NOT_FOUND"
