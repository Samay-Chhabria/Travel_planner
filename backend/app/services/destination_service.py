import re

from app.core.exceptions import NotFoundError
from app.core.logging import get_logger
from app.schemas.destination import Destination
from app.schemas.geocoding import GeocodingResult
from app.services.geocoding_service import search_locations

logger = get_logger(__name__)

DEFAULT_DESTINATION_IMAGE = "https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800&q=80"

_DESTINATION_IMAGE_MAP: dict[str, str] = {
    "paris": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&q=80",
    "tokyo": "https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80",
    "bali": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800&q=80",
    "santorini": "https://images.unsplash.com/photo-1613395877344-13d4a8e0d49e?w=800&q=80",
    "new york": "https://images.unsplash.com/photo-1534430480872-3498386e7856?w=800&q=80",
    "cape town": "https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=800&q=80",
    "barcelona": "https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800&q=80",
    "maldives": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=800&q=80",
    "marrakech": "https://images.unsplash.com/photo-1517821099606-cef63a9baab3?w=800&q=80",
    "iceland": "https://images.unsplash.com/photo-1520769669658-f07657f5a307?w=800&q=80",
    "sydney": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?w=800&q=80",
    "amalfi": "https://images.unsplash.com/photo-1633321702518-7fecdafb94d5?w=800&q=80",
    "thailand": "https://images.unsplash.com/photo-1528181304800-259b08848526?w=800&q=80",
    "patagonia": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&q=80",
    "kyoto": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800&q=80",
    "amsterdam": "https://images.unsplash.com/photo-1534351590666-13e3e96b5017?w=800&q=80",
    "rio de janeiro": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=800&q=80",
    "london": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800&q=80",
    "karachi": "https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800&q=80",
    "rome": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&q=80",
    "dubai": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80",
    "safari": "https://images.unsplash.com/photo-1516426122078-c23e76319801?w=800&q=80",
    "egypt": "https://images.unsplash.com/photo-1539768942893-daf53e736b68?w=800&q=80",
}

_DESTINATION_METADATA_MAP: dict[str, dict] = {
    "london": {
        "description": "Historic capital of England — royal palaces, world-class museums, and a vibrant cultural scene along the Thames.",
        "highlights": ["History", "Culture", "Theatre"],
        "best_time_to_visit": "March to September",
        "travel_type": "City",
    },
    "karachi": {
        "description": "Pakistan's bustling coastal metropolis — colonial architecture, vibrant bazaars, and the Arabian Sea coastline.",
        "highlights": ["Culture", "Food", "Beaches"],
        "best_time_to_visit": "November to February",
        "travel_type": "City",
    },
    "paris": {
        "description": "The City of Light — art, cuisine, and romance along the Seine.",
        "highlights": ["Art", "Food", "Romance"],
        "best_time_to_visit": "April to June",
        "travel_type": "City",
    },
    "tokyo": {
        "description": "Where tradition meets futurism — ancient temples, neon-lit streets, and world-class dining.",
        "highlights": ["Culture", "Food", "Technology"],
        "best_time_to_visit": "March to May",
        "travel_type": "City",
    },
    "rome": {
        "description": "The Eternal City — ancient ruins, Renaissance art, and la dolce vita on every corner.",
        "highlights": ["History", "Art", "Food"],
        "best_time_to_visit": "April to June",
        "travel_type": "City",
    },
    "barcelona": {
        "description": "Gaudí masterpieces, Mediterranean beaches, and vibrant nightlife in Catalonia's capital.",
        "highlights": ["Architecture", "Beach", "Nightlife"],
        "best_time_to_visit": "May to June",
        "travel_type": "City",
    },
    "dubai": {
        "description": "Futuristic skyline, luxury shopping, and desert adventures in the Arabian Gulf.",
        "highlights": ["Luxury", "Shopping", "Architecture"],
        "best_time_to_visit": "November to March",
        "travel_type": "City",
    },
}


def _make_slug(name: str, country: str) -> str:
    raw = f"{name}-{country}".lower().strip()
    return re.sub(r"[^a-z0-9]+", "-", raw).strip("-")


def _infer_travel_type(place_type: str, name: str) -> str:
    t = place_type.lower()
    if "beach" in name.lower() or "island" in t:
        return "Beach"
    if t in ("city", "town", "administrative"):
        return "City"
    if t in ("village", "hamlet", "locality"):
        return "Rural"
    if t in ("mountain", "peak", "ridge"):
        return "Adventure"
    return "City"


def _geocode_to_destination(place) -> Destination:
    slug = _make_slug(place.name, place.country)
    name_key = place.name.lower().strip()
    image_url = _DESTINATION_IMAGE_MAP.get(name_key, DEFAULT_DESTINATION_IMAGE)
    metadata = _DESTINATION_METADATA_MAP.get(name_key, {})
    return Destination(
        id=slug,
        name=place.name,
        country=place.country,
        region=place.region,
        slug=slug,
        latitude=place.latitude,
        longitude=place.longitude,
        description=metadata.get("description", f"Explore {place.name}, {place.country}"),
        image_url=image_url,
        highlights=metadata.get("highlights", [place.region] if place.region else []),
        best_time_to_visit=metadata.get("best_time_to_visit", ""),
        travel_type=metadata.get("travel_type", _infer_travel_type(place.place_type, place.name)),
    )


def _deduplicate_by_name(places: list[GeocodingResult]) -> list[GeocodingResult]:
    """Deduplicate geocoding results by normalized name, keeping the highest-importance result."""
    seen: dict[str, GeocodingResult] = {}
    for place in places:
        key = place.name.lower().strip()
        if key not in seen or place.importance > seen[key].importance:
            seen[key] = place
    return list(seen.values())


_FEATURED_DESTINATIONS: list[Destination] = [
    Destination(
        id="paris-france",
        name="Paris",
        country="France",
        region="Ile-de-France",
        slug="paris-france",
        latitude=48.8566,
        longitude=2.3522,
        description="The City of Light",
        image_url="https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&q=80",
        highlights=["Art", "Food", "Romance"],
        best_time_to_visit="April to June",
        travel_type="City",
    ),
    Destination(
        id="tokyo-japan",
        name="Tokyo",
        country="Japan",
        region="Kanto",
        slug="tokyo-japan",
        latitude=35.6762,
        longitude=139.6503,
        description="Where tradition meets futurism",
        image_url="https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80",
        highlights=["Culture", "Food", "Technology"],
        best_time_to_visit="March to May",
        travel_type="City",
    ),
    Destination(
        id="bali-indonesia",
        name="Bali",
        country="Indonesia",
        region="Lesser Sunda Islands",
        slug="bali-indonesia",
        latitude=-8.3405,
        longitude=115.092,
        description="Island of the Gods",
        image_url="https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800&q=80",
        highlights=["Beaches", "Temples", "Nature"],
        best_time_to_visit="April to October",
        travel_type="Beach",
    ),
    Destination(
        id="santorini-greece",
        name="Santorini",
        country="Greece",
        region="Europe",
        slug="santorini-greece",
        latitude=36.3932,
        longitude=25.4615,
        description="Iconic whitewashed villages overlooking the Aegean Sea",
        image_url="https://images.unsplash.com/photo-1613395877344-13d4a8e0d49e?w=800&q=80",
        highlights=["Scenic", "Romance", "Food"],
        best_time_to_visit="May to September",
        travel_type="Beach",
    ),
    Destination(
        id="new-york-usa",
        name="New York",
        country="United States",
        region="North America",
        slug="new-york-usa",
        latitude=40.7128,
        longitude=-74.0060,
        description="The city that never sleeps — culture, dining, and iconic sights",
        image_url="https://images.unsplash.com/photo-1534430480872-3498386e7856?w=800&q=80",
        highlights=["Culture", "Shopping", "Food"],
        best_time_to_visit="April to June",
        travel_type="City",
    ),
    Destination(
        id="cape-town-south-africa",
        name="Cape Town",
        country="South Africa",
        region="Africa",
        slug="cape-town-south-africa",
        latitude=-33.9249,
        longitude=18.4241,
        description="Stunning coastlines, Table Mountain, and vibrant neighborhoods",
        image_url="https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=800&q=80",
        highlights=["Nature", "Adventure", "Scenic"],
        best_time_to_visit="November to March",
        travel_type="Adventure",
    ),
    Destination(
        id="london-united-kingdom",
        name="London",
        country="United Kingdom",
        region="England",
        slug="london-united-kingdom",
        latitude=51.5074,
        longitude=-0.1278,
        description="Historic capital of England — royal palaces, world-class museums, and a vibrant cultural scene along the Thames.",
        image_url="https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800&q=80",
        highlights=["History", "Culture", "Theatre"],
        best_time_to_visit="March to September",
        travel_type="City",
    ),
    Destination(
        id="karachi-pakistan",
        name="Karachi",
        country="Pakistan",
        region="Sindh",
        slug="karachi-pakistan",
        latitude=24.8607,
        longitude=67.0011,
        description="Pakistan's bustling coastal metropolis — colonial architecture, vibrant bazaars, and the Arabian Sea coastline.",
        image_url="https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800&q=80",
        highlights=["Culture", "Food", "Beaches"],
        best_time_to_visit="November to February",
        travel_type="City",
    ),
]


async def search_destinations(
    query: str,
    limit: int = 10,
    country_code: str | None = None,
) -> list[Destination]:
    """Search for destinations using geocoding provider, normalized to Destination objects."""
    logger.info("Destination search: query='%s' limit=%d country=%s", query, limit, country_code)
    places = await search_locations(query=query, limit=limit, country_code=country_code)
    unique_places = _deduplicate_by_name(places)
    return [_geocode_to_destination(p) for p in unique_places]


async def get_destination_by_id(destination_id: str) -> Destination:
    """Get a single destination by id or slug. Checks featured list first, then geocodes."""
    for dest in _FEATURED_DESTINATIONS:
        if dest.id == destination_id or dest.slug == destination_id:
            return dest

    query = destination_id.replace("-", " ")
    places = await search_locations(query=query, limit=1)
    if places:
        return _geocode_to_destination(places[0])

    raise NotFoundError(f"Destination not found for '{destination_id}'")


def get_featured_destinations(limit: int = 6) -> list[Destination]:
    """Return curated featured destinations for the landing page."""
    return _FEATURED_DESTINATIONS[:limit]
