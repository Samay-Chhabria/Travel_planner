import asyncio
import uuid
from datetime import date, timedelta

from app.core.exceptions import NotFoundError, UpstreamProviderError
from app.core.logging import get_logger
from app.schemas.trip_plan import ActivityItem, DayPlan, TripPlan
from app.services.attraction_service import get_attractions_for_destination
from app.services.destination_service import search_destinations
from app.services.hotel_service import get_hotels_for_destination
from app.services.restaurant_service import get_restaurants_for_destination
from app.services.weather_service import get_weather_for_destination

logger = get_logger(__name__)

_STYLE_TEMPLATES: dict[str, dict] = {
    "culture": {
        "summary": "A cultural immersion with museum visits, historic landmarks, and local experiences.",
        "morning": [
            "Visit a major museum or gallery",
            "Explore the historic district on foot",
            "Join a guided walking tour of landmarks",
        ],
        "afternoon": [
            "Visit a local cultural center or exhibition",
            "Explore a neighborhood known for its heritage",
            "Attend a local craft or art workshop",
        ],
        "evening": [
            "Dinner at a traditional local restaurant",
            "Attend a live performance or concert",
            "Evening stroll through illuminated streets",
        ],
        "notes": "Check museum opening days and book skip-the-line tickets where possible.",
    },
    "adventure": {
        "summary": "An active itinerary packed with outdoor exploration and thrilling experiences.",
        "morning": [
            "Early morning hike or nature walk",
            "Visit a scenic viewpoint or overlook",
            "Try a water sport or cycling tour",
        ],
        "afternoon": [
            "Explore a national park or trail",
            "Visit an adventure activity center",
            "Discover a waterfall or natural landmark",
        ],
        "evening": [
            "Casual dinner with local flavors",
            "Sunset viewing at a scenic spot",
            "Campfire stories or stargazing if possible",
        ],
        "notes": "Wear comfortable shoes and carry water. Check weather conditions for outdoor activities.",
    },
    "food": {
        "summary": "A culinary journey through local markets, restaurants, and food traditions.",
        "morning": [
            "Visit a local food market or farmer's market",
            "Enjoy a traditional breakfast at a local cafe",
            "Take a neighborhood food walking tour",
        ],
        "afternoon": [
            "Attend a cooking class with local cuisine",
            "Lunch at a highly-rated local restaurant",
            "Explore street food stalls and snack vendors",
        ],
        "evening": [
            "Dinner at a signature restaurant of the region",
            "Try a local food experience or tasting menu",
            "Visit a rooftop bar or dessert spot",
        ],
        "notes": "Make restaurant reservations in advance for popular spots. Bring an appetite!",
    },
    "relaxation": {
        "summary": "A leisurely escape focused on unwinding, scenic beauty, and gentle exploration.",
        "morning": [
            "Sleep in and enjoy a leisurely breakfast",
            "Relax at a spa or wellness center",
            "Gentle morning yoga or meditation session",
        ],
        "afternoon": [
            "Stroll through a botanical garden or park",
            "Enjoy a scenic boat ride or light walk",
            "Relax at a beach or lakeside spot",
        ],
        "evening": [
            "Sundowner drinks with a view",
            "Light dinner at a waterfront restaurant",
            "Evening bath or hot spring visit",
        ],
        "notes": "No rush today. Let the destination come to you at a comfortable pace.",
    },
    "general": {
        "summary": "A balanced mix of sightseeing, culture, food, and leisure.",
        "morning": [
            "Visit a top landmark or attraction",
            "Explore a lively local neighborhood",
            "Stop at a popular cafe for breakfast",
        ],
        "afternoon": [
            "Lunch at a well-reviewed local spot",
            "Visit a museum or cultural site",
            "Shop for souvenirs or local crafts",
        ],
        "evening": [
            "Dinner at a restaurant with local specialties",
            "Evening walk through a scenic area",
            "Enjoy local nightlife or a rooftop view",
        ],
        "notes": "Keep the pace flexible. Mix must-see sights with spontaneous discoveries.",
    },
}

_ARRIVAL_ACTIVITY = "Arrive and check in to accommodation"
_DEPARTURE_ACTIVITY = "Check out and depart"

_DAY_TITLE_TEMPLATES: list[str] = [
    "Arrival and First Impressions",
    "Exploring {place}",
    "Deep Dive into {place}",
    "Hidden Gems of {place}",
    "Culture and Cuisine Day",
    "Adventure and Discovery",
    "Local Life Experience",
    "Relaxation and Reflection",
    "Final Exploration",
    "Farewell to {place}",
]

_BUDGET_TWEAKS: dict[str, str] = {
    "budget": "Look for free walking tours, street food, and public transport passes.",
    "moderate": "Mix paid attractions with free exploration. Mid-range dining is a great choice.",
    "luxury": "Consider private tours, fine dining, and premium experiences for a memorable trip.",
}


def _get_style_template(style: str) -> dict:
    return _STYLE_TEMPLATES.get(style.lower(), _STYLE_TEMPLATES["general"])


def _build_weather_summary(weather_data) -> str:
    if not weather_data or not weather_data.forecast:
        return "Weather data is not available for this destination."
    temps = [f.max_temp_c for f in weather_data.forecast]
    conditions = list({f.condition for f in weather_data.forecast})
    avg = sum(temps) / len(temps) if temps else 0
    return f"Expect around {avg:.0f}C average with {', '.join(conditions[:3])} conditions."


def _generate_day_plan(
    day_num: int,
    current_date: date,
    template: dict,
    place_name: str,
    total_days: int,
) -> DayPlan:
    if day_num == 1:
        title = _DAY_TITLE_TEMPLATES[0]
        activities = [
            ActivityItem(time="10:00", description=_ARRIVAL_ACTIVITY),
            ActivityItem(time="14:00", description="Take a short walk around the neighborhood"),
            ActivityItem(time="19:00", description="Enjoy a relaxed welcome dinner"),
        ]
        notes = "Keep the first day light to settle in and get oriented."
    elif day_num == total_days:
        title = _DAY_TITLE_TEMPLATES[-1].replace("{place}", place_name)
        activities = [
            ActivityItem(time="09:00", description="Last-minute souvenir shopping"),
            ActivityItem(time="12:00", description="Farewell lunch at a favorite spot"),
            ActivityItem(time="15:00", description=_DEPARTURE_ACTIVITY),
        ]
        notes = "Double-check your belongings and confirm transport to the airport or station."
    else:
        idx = min(day_num - 1, len(_DAY_TITLE_TEMPLATES) - 3)
        title = _DAY_TITLE_TEMPLATES[idx].replace("{place}", place_name)
        pool = template.get("morning", []) + template.get("afternoon", []) + template.get("evening", [])
        morning_pick = pool[(day_num * 3) % len(pool)] if pool else "Explore at your own pace"
        afternoon_pick = pool[(day_num * 3 + 1) % len(pool)] if pool else "Enjoy local cuisine"
        evening_pick = pool[(day_num * 3 + 2) % len(pool)] if pool else "Evening at leisure"
        activities = [
            ActivityItem(time="09:00", description=morning_pick),
            ActivityItem(time="13:00", description=afternoon_pick),
            ActivityItem(time="19:00", description=evening_pick),
        ]
        notes = template.get("notes", "")

    return DayPlan(
        day=day_num,
        date=current_date,
        title=title,
        activities=activities,
        notes=notes,
    )


def _build_plan(
    destination,
    request,
    weather_data,
    attractions,
    hotels,
    restaurants,
) -> TripPlan:
    style = request.travel_style or "general"
    budget = request.budget_level or "moderate"
    template = _get_style_template(style)

    duration = (request.end_date - request.start_date).days + 1
    plan_id = f"plan-{uuid.uuid4().hex[:12]}"
    place_name = destination.name

    days: list[DayPlan] = []
    for i in range(duration):
        d = request.start_date + timedelta(days=i)
        days.append(_generate_day_plan(i + 1, d, template, place_name, duration))

    weather_summary = _build_weather_summary(weather_data)
    top_attractions = [a.name for a in attractions[:5]]
    top_hotels = [h.name for h in hotels[:3]]
    top_restaurants = [r.name for r in restaurants[:3]]

    summary = f"{template['summary']} { _BUDGET_TWEAKS.get(budget, '') }"

    return TripPlan(
        id=plan_id,
        destination=place_name,
        country=destination.country,
        duration_days=duration,
        travel_style=style,
        budget_level=budget,
        group_type=request.group_type,
        summary=summary,
        days=days,
        weather_summary=weather_summary,
        top_attractions=top_attractions,
        recommended_hotels=top_hotels,
        recommended_restaurants=top_restaurants,
    )


async def _safe_fetch(coro):
    try:
        return await coro
    except (NotFoundError, UpstreamProviderError) as exc:
        logger.warning("Service fetch failed (non-fatal): %s", exc)
        return None


async def generate_trip_plan(request) -> TripPlan:
    """Generate a rule-based trip plan by orchestrating existing services.

    Fetches destination info, weather, attractions, hotels, and restaurants
    in parallel. Partial failures are handled gracefully — missing data is
    replaced with empty defaults.
    """
    logger.info(
        "Generating trip plan: destination='%s' style='%s' budget='%s'",
        request.destination, request.travel_style, request.budget_level,
    )

    results = await search_destinations(query=request.destination, limit=1)
    if not results:
        raise NotFoundError(f"Destination not found for '{request.destination}'")
    destination = results[0]
    dest_id = destination.slug
    duration = (request.end_date - request.start_date).days + 1

    weather_task = _safe_fetch(get_weather_for_destination(dest_id, days=min(duration, 16)))
    attractions_task = _safe_fetch(get_attractions_for_destination(dest_id, limit=10))
    hotels_task = _safe_fetch(get_hotels_for_destination(dest_id, limit=10, budget=request.budget_level))
    restaurants_task = _safe_fetch(get_restaurants_for_destination(dest_id, limit=10))

    weather_data, attractions, hotels, restaurants = await asyncio.gather(
        weather_task, attractions_task, hotels_task, restaurants_task,
    )

    attractions = attractions or []
    hotels = hotels or []
    restaurants = restaurants or []

    return _build_plan(destination, request, weather_data, attractions, hotels, restaurants)
