# Travel Planner Backend

FastAPI backend for the Travel Planner MVP. Acts as an API gateway that aggregates free travel APIs (Open-Meteo, Nominatim, OpenTripMap) and returns clean, normalized JSON to the React frontend.

## Setup

```bash
cd backend
python -m venv travelvenv

# Windows
travelvenv\Scripts\activate

# macOS / Linux
source travelvenv/bin/activate

pip install -r requirements.txt
cp .env.example .env   # fill in OPENTRIPMAP_API_KEY for live data
```

## Run

```bash
uvicorn app.main:app --reload --port 8000
```

API base URL: http://localhost:8000/api/v1
Health check: http://localhost:8000/health
Auto-generated docs: http://localhost:8000/docs

## Test

```bash
pytest
```

## Environment Variables

| Variable | Default | Description |
|---|---|---|
| `ENVIRONMENT` | `development` | Application environment |
| `API_HOST` | `0.0.0.0` | Server host |
| `API_PORT` | `8000` | Server port |
| `CORS_ORIGINS` | `http://localhost:5173,http://localhost:3000` | Allowed CORS origins |
| `OPENTRIPMAP_API_KEY` | `""` | OpenTripMap API key (required for attractions/hotels/restaurants) |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Health check |
| GET | `/api/v1/destinations/search` | Search destinations |
| GET | `/api/v1/destinations/{id}` | Destination details |
| GET | `/api/v1/destinations/featured` | Featured destinations |
| GET | `/api/v1/geocoding/search` | Geocoding search |
| GET | `/api/v1/destinations/{id}/weather` | Weather data |
| GET | `/api/v1/destinations/{id}/attractions` | Nearby attractions |
| GET | `/api/v1/destinations/{id}/restaurants` | Nearby restaurants |
| GET | `/api/v1/destinations/{id}/hotels` | Nearby hotels |
| POST | `/api/v1/trip-planner/generate` | Generate trip plan |

## Project Structure

```text
backend/
├── app/
│   ├── api/routes/        # Endpoint definitions
│   ├── core/              # Config, exceptions, logging, middleware
│   ├── integrations/      # External API adapters (Open-Meteo, Nominatim, OpenTripMap)
│   ├── schemas/           # Pydantic request/response models
│   ├── services/          # Business logic and orchestration
│   ├── utils/             # Shared helpers (HTTP, response formatting)
│   └── main.py            # FastAPI application entry point
├── tests/                 # pytest test suite
├── .env.example           # Environment variable template
├── pyproject.toml         # pytest configuration
├── requirements.txt       # Python dependencies
└── README.md
```
