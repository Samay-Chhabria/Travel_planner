# REST API Specification - Travel Planner MVP

## 1. Purpose

This document defines the complete REST API specification for the Travel Planner MVP. It is aligned with the PRD, project context, software architecture, UI/UX strategy, and component library requirements.

The API is designed as a thin backend gateway that:
- receives frontend requests
- validates input
- calls one or more free travel and mapping providers
- normalizes and aggregates responses
- returns clean, predictable JSON to the frontend

This specification is intentionally production-oriented, but still scoped to the MVP and does not require authentication, persistence, or AI features.

---

## 2. API Goals

### 2.1 Functional Goals
- Enable destination discovery
- Provide destination details and travel context
- Return weather, attractions, restaurants, hotels, and map context
- Generate a simple rule-based trip plan
- Support graceful error handling and consistent responses

### 2.2 Non-Functional Goals
- Simple and maintainable API structure
- Clear versioning strategy
- Consistent response contracts
- Fast enough for a portfolio-ready MVP
- Easy to extend in future phases

---

## 3. Architectural Principles

- RESTful resource-oriented design
- Backend acts as an API gateway
- Frontend never calls third-party APIs directly
- Validation occurs on the server
- Standardized response schemas
- Consistent error handling
- Free/open APIs are preferred

---

## 4. API Base Information

### 4.1 Base URL
- Development: http://localhost:8000/api/v1
- Production: https://<backend-host>/api/v1

### 4.2 Versioning
- API versioning is handled through the URL prefix: /api/v1

### 4.3 Content Type
- Request/response: application/json

### 4.4 Authentication
- Not required for MVP
- No user sessions, tokens, or API keys for frontend users

### 4.5 CORS
- Allowed origins should be configured explicitly for frontend deployment

---

## 5. API Conventions

### 5.1 Resource Naming
- Use lowercase plural nouns for collections
- Use path parameters for resource identifiers
- Use query parameters for filtering, searching, and pagination

### 5.2 HTTP Methods
- GET: retrieve data
- POST: create or trigger a computation or plan generation
- PUT/PATCH: not required in MVP
- DELETE: not required in MVP

### 5.3 Response Format
All successful responses should follow a consistent structure:

```json
{
  "success": true,
  "data": {},
  "message": "Request completed successfully"
}
```

### 5.4 Error Response Format
All errors should follow a consistent structure:

```json
{
  "success": false,
  "error": {
    "code": "INVALID_REQUEST",
    "message": "The destination query is required.",
    "details": []
  }
}
```

---

## 6. Common Status Codes

| Status Code | Meaning |
|---|---|
| 200 | Request succeeded |
| 201 | Resource created successfully |
| 400 | Invalid request or validation error |
| 404 | Resource not found |
| 422 | Request validation failed |
| 429 | Too many requests |
| 500 | Internal server error |
| 502 | Upstream provider failure |
| 503 | Service temporarily unavailable |

---

## 7. Common Data Models

### 7.1 Destination
```json
{
  "id": "string",
  "name": "string",
  "country": "string",
  "region": "string",
  "slug": "string",
  "latitude": 0.0,
  "longitude": 0.0,
  "description": "string",
  "image_url": "string",
  "highlights": ["string"],
  "best_time_to_visit": "string",
  "travel_type": "string"
}
```

### 7.2 Weather Summary
```json
{
  "destination_id": "string",
  "current": {
    "temperature_c": 0,
    "temperature_f": 0,
    "condition": "string",
    "description": "string"
  },
  "forecast": [
    {
      "date": "YYYY-MM-DD",
      "max_temp_c": 0,
      "min_temp_c": 0,
      "condition": "string"
    }
  ]
}
```

### 7.3 Attraction
```json
{
  "id": "string",
  "name": "string",
  "category": "string",
  "description": "string",
  "address": "string",
  "latitude": 0.0,
  "longitude": 0.0,
  "image_url": "string",
  "rating": 0.0
}
```

### 7.4 Restaurant
```json
{
  "id": "string",
  "name": "string",
  "cuisine_type": "string",
  "description": "string",
  "address": "string",
  "price_level": "string",
  "rating": 0.0,
  "image_url": "string",
  "latitude": 0.0,
  "longitude": 0.0
}
```

### 7.5 Hotel
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "address": "string",
  "latitude": 0.0,
  "longitude": 0.0,
  "image_url": "string",
  "rating": 0.0,
  "price_level": "string",
  "star_rating": 0
}
```

### 7.6 Trip Plan
```json
{
  "id": "string",
  "destination": "string",
  "country": "string",
  "duration_days": 0,
  "travel_style": "string",
  "budget_level": "string",
  "group_type": "string",
  "summary": "string",
  "days": [
    {
      "day": 1,
      "date": "YYYY-MM-DD",
      "title": "string",
      "activities": [
        {"time": "09:00", "description": "string"}
      ],
      "notes": "string"
    }
  ],
  "weather_summary": "string",
  "top_attractions": ["string"],
  "recommended_hotels": ["string"],
  "recommended_restaurants": ["string"]
}
```

---

## 8. Endpoint Specification

## 8.1 Health and Status

### GET /health
Returns server health information.

**Purpose**
- Verify service availability
- Support deployment checks

**Response**
```json
{
  "success": true,
  "data": {
    "status": "ok",
    "service": "travel-planner-api",
    "version": "v1"
  },
  "message": "Service is healthy"
}
```

---

## 8.2 Destination Discovery

### GET /destinations/search
Search destinations by query.

**Purpose**
- Support destination search experience on the landing and explore pages

**Query Parameters**
- q: required, string, minimum 2 characters
- country: optional, string
- limit: optional, integer, default 10
- page: optional, integer, default 1

**Example Request**
GET /api/v1/destinations/search?q=paris&limit=5

**Success Response**
```json
{
  "success": true,
  "data": {
    "results": [
      {
        "id": "paris-france",
        "name": "Paris",
        "country": "France",
        "region": "Europe",
        "slug": "paris-france",
        "latitude": 48.8566,
        "longitude": 2.3522,
        "description": "The City of Light",
        "image_url": "https://example.com/paris.jpg",
        "highlights": ["Art", "Food", "Romance"],
        "best_time_to_visit": "April to June",
        "travel_type": "City"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 5,
      "total": 1
    }
  },
  "message": "Destinations retrieved successfully"
}
```

**Error Cases**
- Missing q: 400 or 422
- No results: 200 with empty results array

---

### GET /destinations/{destination_id}
Get a single destination by id or slug.

**Purpose**
- Render the destination details page

**Path Parameters**
- destination_id: required string

**Success Response**
```json
{
  "success": true,
  "data": {
    "destination": {
      "id": "paris-france",
      "name": "Paris",
      "country": "France",
      "region": "Europe",
      "slug": "paris-france",
      "latitude": 48.8566,
      "longitude": 2.3522,
      "description": "The City of Light",
      "image_url": "https://example.com/paris.jpg",
      "highlights": ["Art", "Food", "Romance"],
      "best_time_to_visit": "April to June",
      "travel_type": "City"
    }
  },
  "message": "Destination details retrieved successfully"
}
```

**Error Cases**
- Unknown destination: 404

---

### GET /destinations/featured
Retrieve featured destinations for landing page hero or featured cards.

**Purpose**
- Power featured destination sections on the landing page

**Query Parameters**
- limit: optional, integer, default 6

**Success Response**
```json
{
  "success": true,
  "data": {
    "destinations": []
  },
  "message": "Featured destinations retrieved successfully"
}
```

---

## 8.3 Geocoding

### GET /geocoding/search
Search for geographic locations by name. Returns geocoded results with coordinates.

**Purpose**
- Internal utility endpoint for destination lookup and geocoding
- Powers the destination search and geocode fallback in the destination service

**Query Parameters**
- q: required, string, minimum 2 characters
- country: optional, string, ISO 3166-1 alpha-2 country code filter
- limit: optional, integer, default 10
- page: optional, integer, default 1

**Example Request**
GET /api/v1/geocoding/search?q=paris&limit=5

**Success Response**
```json
{
  "success": true,
  "data": {
    "results": [
      {
        "id": "97683695",
        "name": "Paris",
        "display_name": "Paris, Ile-de-France, Metropolitan France, France",
        "latitude": 48.853,
        "longitude": 2.348,
        "country": "France",
        "country_code": "fr",
        "region": "Ile-de-France",
        "city": "Paris",
        "place_type": "administrative",
        "importance": 0.897
      }
    ],
    "query": "paris",
    "pagination": {
      "page": 1,
      "limit": 5,
      "total": 1
    }
  },
  "message": "Locations retrieved successfully"
}
```

**Error Cases**
- Missing q: 400 or 422
- No results: 200 with empty results array
- Upstream provider unavailable: 502

---

## 8.4 Weather

### GET /destinations/{destination_id}/weather
Get weather context for a destination.

**Purpose**
- Support the weather section on the destination details page

**Path Parameters**
- destination_id: required string

**Query Parameters**
- days: optional integer, default 5

**Success Response**
```json
{
  "success": true,
  "data": {
    "weather": {
      "destination_id": "paris-france",
      "current": {
        "temperature_c": 21,
        "temperature_f": 70,
        "condition": "Clear",
        "description": "Sunny conditions"
      },
      "forecast": [
        {
          "date": "2026-07-12",
          "max_temp_c": 24,
          "min_temp_c": 16,
          "condition": "Clear"
        }
      ]
    }
  },
  "message": "Weather data retrieved successfully"
}
```

**Error Cases**
- Missing or invalid destination: 404
- Upstream provider unavailable: 502 or 503

---

## 8.5 Attractions

### GET /destinations/{destination_id}/attractions
Get attractions for a destination.

**Purpose**
- Render the attractions section on the destination details page

**Query Parameters**
- limit: optional integer, default 8
- category: optional string

**Success Response**
```json
{
  "success": true,
  "data": {
    "attractions": []
  },
  "message": "Attractions retrieved successfully"
}
```

---

## 8.6 Restaurants

### GET /destinations/{destination_id}/restaurants
Get restaurants near a destination.

**Purpose**
- Display food-related content on destination detail pages

**Query Parameters**
- limit: optional integer, default 8
- cuisine: optional string

**Success Response**
```json
{
  "success": true,
  "data": {
    "restaurants": []
  },
  "message": "Restaurants retrieved successfully"
}
```

---

## 8.7 Hotels

### GET /destinations/{destination_id}/hotels
Get hotel suggestions for a destination.

**Purpose**
- Support hotel recommendations in the destination details experience

**Query Parameters**
- limit: optional integer, default 6
- budget: optional string

**Success Response**
```json
{
  "success": true,
  "data": {
    "hotels": []
  },
  "message": "Hotels retrieved successfully"
}
```

---

## 8.8 Trip Planning

### POST /trip-planner/generate
Generate a simple rule-based travel plan.

**Purpose**
- Power the trip planner page

**Request Body**
```json
{
  "destination": "Paris",
  "start_date": "2026-08-01",
  "end_date": "2026-08-05",
  "travel_style": "culture",
  "budget_level": "moderate",
  "group_type": "couple"
}
```

**Validation Rules**
- destination: required, non-empty string
- start_date: required, valid date
- end_date: required, valid date
- end_date must be after or equal to start_date
- travel_style: optional string
- budget_level: optional string
- group_type: optional string

**Success Response**
```json
{
  "success": true,
  "data": {
    "plan": {
      "id": "plan-a1b2c3d4e5f6",
      "destination": "Paris",
      "country": "France",
      "duration_days": 5,
      "travel_style": "culture",
      "budget_level": "moderate",
      "group_type": "couple",
      "summary": "A cultural immersion with museum visits, historic landmarks, and local experiences. Mix paid attractions with free exploration. Mid-range dining is a great choice.",
      "days": [
        {
          "day": 1,
          "date": "2026-08-01",
          "title": "Arrival and First Impressions",
          "activities": [
            {"time": "10:00", "description": "Arrive and check in to accommodation"},
            {"time": "14:00", "description": "Take a short walk around the neighborhood"},
            {"time": "19:00", "description": "Enjoy a relaxed welcome dinner"}
          ],
          "notes": "Keep the first day light to settle in and get oriented."
        }
      ],
      "weather_summary": "Expect around 25C average with Sunny, Cloudy conditions.",
      "top_attractions": ["Louvre Museum", "Eiffel Tower"],
      "recommended_hotels": ["Grand Hotel Paris"],
      "recommended_restaurants": ["Le Petit Bistro"]
    }
  },
  "message": "Trip plan generated successfully"
}
```

**Error Cases**
- Missing destination: 422
- Invalid date range: 422
- Destination not found: 404
- Planner generation failure: 500 or 502

---

## 8.9 Contact Endpoint (Deferred)

### POST /contact
Submit a contact message from the contact page.

**Purpose**
- Support the contact form experience

**Request Body**
```json
{
  "name": "Ava",
  "email": "ava@example.com",
  "message": "I would love to learn more about the project."
}
```

**Success Response**
```json
{
  "success": true,
  "data": {
    "submitted": true
  },
  "message": "Message received successfully"
}
```

**Note**
- This endpoint is deferred from the MVP.
- The frontend contact form currently operates as a frontend-only experience without backend submission.
- Can be implemented as a stub or email-forwarding integration in a later phase.

---

## 9. Pagination and Filtering

Where list endpoints return multiple items, the following pattern should be used:

```json
{
  "success": true,
  "data": {
    "results": [],
    "pagination": {
      "page": 1,
      "limit": 10,
      "total": 0
    }
  }
}
```

Recommended defaults:
- page = 1
- limit = 10

---

## 10. Error Handling Strategy

### 10.1 Validation Errors
Used when request data is missing or malformed.

Example:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Request validation failed",
    "details": [
      {
        "field": "destination",
        "issue": "Field is required"
      }
    ]
  }
}
```

### 10.2 Provider Errors
Used when upstream services fail.

Example:
```json
{
  "success": false,
  "error": {
    "code": "UPSTREAM_PROVIDER_ERROR",
    "message": "Weather provider is temporarily unavailable"
  }
}
```

### 10.3 Not Found Errors
Used for unknown destinations or missing resources.

Example:
```json
{
  "success": false,
  "error": {
    "code": "NOT_FOUND",
    "message": "Destination could not be found"
  }
}
```

---

## 11. Security and Operational Considerations

### 11.1 MVP Security Scope
- No authentication required
- No user accounts
- No sensitive data handling beyond public travel data
- All third-party secrets must remain server-side only

### 11.2 Reliability
- Timeouts for upstream provider calls
- Graceful degradation when one provider fails
- Consistent fallback messages for the frontend

### 11.3 Logging
The backend should log:
- request start and completion
- validation failures
- provider errors
- unexpected exceptions

---

## 12. Frontend Integration Expectations

The frontend should consume these endpoints through a centralized API client layer.

### Frontend Implementation Status

All frontend pages are now fully integrated with the backend API. Zero mock data remains in production code.

- **API Client:** `apiClient.js` — Axios instance configured with `VITE_API_BASE_URL`, includes request/response interceptors and centralized error handling (timeout, network, and server error normalization)
- **Generic Hook:** `useFetch.js` — reusable data-fetching hook with loading/error state management and manual execute capability
- **Destination Service:** `destinationService.js` — `getFeaturedDestinations`, `searchDestinations`, `getDestinationById`
- **Weather Service:** `weatherService.js` — `getWeatherForDestination(destinationId, days)`
- **Attractions Service:** `attractionsService.js` — `getAttractionsForDestination(destinationId, options)`
- **Restaurants Service:** `restaurantsService.js` — `getRestaurantsForDestination(destinationId, options)`
- **Hotels Service:** `hotelsService.js` — `getHotelsForDestination(destinationId, options)`
- **Planner Service:** `plannerService.js` — `generateTripPlan(planRequest)`

All services unwrap the `{ success, data, message }` envelope and return the inner `data` payload directly. Errors are propagated as `Error` objects with human-readable messages.

**Explore page:** Uses API exclusively — `getFeaturedDestinations(20)` loads initial data, `searchDestinations(query, { limit: 25 })` powers live search with debounce. Client-side filtering by travel type and region applied on API results.

**Destination Details page:** Uses `getDestinationById(slug)` via `useFetch` hook with full loading skeleton and error states. All sub-sections (Weather, Attractions, Hotels, Restaurants) fetch data independently using `destinationId`.

**Weather Widget:** Uses `getWeatherForDestination(destinationId)` via `useFetch` hook. Displays current conditions and multi-day forecast. Loading skeleton, error retry, and empty states implemented.

**Hotels/Restaurants/Attractions sections:** Each uses its respective service via `useFetch` hook with `useCallback` for memoization. All have loading skeletons, error retry buttons, and empty state messages.

**Trip Planner:** Uses `generateTripPlan()` with field mapping (theme → travel_style, budget → budget_level, travelers → group_type). Loading state, error display with retry, and full itinerary rendering from API response.

**Featured Destinations (Home):** Uses `getFeaturedDestinations(6)` with `FALLBACK_FEATURED_DESTINATIONS` for offline/error fallback.

**404 page:** Implemented `NotFoundPage` with catch-all route `*` in React Router.

### Expected frontend behavior
- Display loading states while requests are in progress
- Show empty states when no results are returned
- Display friendly error messages for failed requests
- Keep UI components decoupled from provider-specific response details

---

## 13. Recommended Response Contract Summary

To keep the frontend consistent, every endpoint should return:
- success boolean
- data object or array
- message string
- error object when unsuccessful

This contract should remain stable even as backend providers change.

---

## 14. Future API Extensions

Future phases may extend this API with:
- authentication and user-specific endpoints
- saved trips and profile management
- AI itinerary generation
- richer itinerary editing flows
- booking-related features

These should be added as versioned extensions rather than breaking the existing MVP contract.

---

## 15. Implementation Notes for the Backend Team

The backend API has been implemented using:
- FastAPI with factory pattern (`create_app()`)
- Pydantic v2 models for validation and serialization
- Route-based organization by concern (`app/api/routes/`)
- Service layer for provider orchestration (`app/services/`)
- Integration layer for third-party API clients (`app/integrations/providers/`)

The frontend should interact with this API only; direct third-party calls are not part of the architecture.
