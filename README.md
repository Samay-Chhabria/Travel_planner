# Travel Planner

A modern, Airbnb-inspired travel discovery and planning application built with React + Vite + Tailwind CSS (frontend) and FastAPI (backend).

## Project Overview

Travel Planner is a portfolio project and prompt engineering learning exercise. The application lets users discover travel destinations, explore details (weather, attractions, restaurants, hotels), and generate simple rule-based trip itineraries.

**Phase 1 (MVP)** focuses on a beautiful, responsive frontend and a clean FastAPI backend. AI features, authentication, databases, and payments are deferred to future phases.

## Tech Stack

### Frontend

- **React 18** with Vite 6
- **Tailwind CSS 3** with custom design tokens
- **React Router 6** for client-side routing
- **Axios** for API communication

### Backend

- **FastAPI** with Pydantic v2 validation
- **Uvicorn** as ASGI server
- **httpx** for async HTTP requests to external APIs
- Free travel API integrations (Open-Meteo, Nominatim, OpenTripMap)

### Deployment

- **Frontend:** Vercel (static build from `frontend/dist`)
- **Backend:** Render (Uvicorn)
- Deployment configs: `vercel.json` (root), `render.yaml` (root)

## Project Structure

```text
travel-planner/
├── frontend/          # React + Vite + Tailwind CSS
│   ├── src/
│   │   ├── pages/         # Route-level page components
│   │   ├── components/    # Reusable UI components
│   │   │   ├── common/        # Button, Badge, Input, StarRating, etc.
│   │   │   ├── layout/        # Navbar, Footer, PageContainer, SectionWrapper
│   │   │   ├── cards/         # DestinationCard, ThemeCard, TestimonialCard
│   │   │   ├── search/        # SearchBar, FilterBar, SortSelect, ViewToggle
│   │   │   ├── destination/   # DestinationHero, WeatherWidget, AttractionsSection, etc.
│   │   │   ├── planner/       # DestinationSelector, DatePicker, ThemeSelector, etc.
│   │   │   ├── contact/       # ContactForm, ContactInfo, FAQSection, SocialLinks
│   │   │   ├── about/         # HeroSection, MissionSection, FeaturesSection, etc.
│   │   │   ├── sections/      # Landing page sections (Hero, Featured, Themes, Testimonials)
│   │   │   └── feedback/      # EmptyState, ErrorState, LoadingState
│   │   ├── services/      # API client and service modules
│   │   ├── hooks/         # Custom React hooks (useDebounce, useFetch)
│   │   ├── utils/         # Utilities (constants, validators, dateUtils)
│   │   ├── routes/        # Route definitions with React.lazy code splitting
│   │   ├── layouts/       # MainLayout
│   │   └── styles/        # Tailwind imports, CSS variables
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── package.json
├── backend/           # FastAPI API gateway
│   ├── app/
│   │   ├── api/routes/        # Endpoint definitions
│   │   ├── services/          # Business logic
│   │   ├── schemas/           # Pydantic models
│   │   ├── integrations/      # External API adapters
│   │   ├── core/              # Config, exceptions, logging
│   │   └── utils/             # Shared helpers
│   ├── tests/                 # pytest test suite (157 tests)
│   ├── .env.example           # Backend env var template
│   ├── pyproject.toml         # pytest configuration
│   └── requirements.txt
├── Docs/              # Product, design, and architecture specs
├── vercel.json        # Vercel deployment config (frontend)
├── render.yaml        # Render deployment config (backend)
├── .env.example       # Environment variable template
├── .gitignore
└── README.md
```

## Features Completed

### Frontend Milestone — Complete

| Page | Status | Key Components |
|---|---|---|
| Landing Page (`/`) | Done | Hero, SearchBar, FeaturedDestinations, PopularThemes, Testimonials |
| Explore Page (`/explore`) | Done | SearchBar, FilterBar, SortSelect, ViewToggle, DestinationCard grid, empty/loading/error states |
| Destination Details (`/destinations/:slug`) | Done | Hero, Overview, WeatherWidget, AttractionsSection, RestaurantsSection, HotelsSection, MapPlaceholder, PlanTripCTA |
| Trip Planner (`/planner`) | Done | DestinationSelector, DatePicker, BudgetSelector, TravelersSelector, ThemeSelector, TripSummary, ItineraryPlaceholder |
| About Page (`/about`) | Done | Hero, Mission, Features, TechStack, Team sections |
| Contact Page (`/contact`) | Done | ContactForm, ContactInfo, SocialLinks, FAQSection |

### Shared Components

- **Common:** Button, Badge, Input, StarRating, PriceLevel, SectionHeader, DetailCard
- **Feedback:** EmptyState, ErrorState, LoadingState (skeletons)
- **Layout:** Navbar (sticky, mobile menu, skip-to-content), Footer, PageContainer, SectionWrapper

### Design System

- Custom Tailwind tokens: `background`, `surface`, `primary`, `secondary`, `accent`, `highlight`, `border`, `error`, `star`, `rain`
- Custom shadows: `card`, `card-hover`, `elevated`, `nav`
- Custom border-radius: `card` (1.125rem), `pill` (9999px)
- DM Sans font family
- Responsive across mobile, tablet, and desktop

### Performance

- React.lazy + Suspense code splitting on all routes
- useMemo for expensive filtering operations
- Native lazy loading on images (`loading="lazy"`)
- Debounced search input to reduce API calls

### Accessibility

- Skip-to-content link in Navbar
- ARIA labels on search inputs and interactive elements
- aria-expanded/aria-controls on FAQ accordions
- Semantic HTML structure with proper heading hierarchy
- Visible focus states and keyboard navigation support

## Installation

### Prerequisites

- **Node.js** 18 or later
- **npm** 9 or later
- **Python** 3.11 or later (for backend)

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env   # optional — defaults work for local dev
npm run dev
```

Open [http://localhost:5173](http://localhost:5173)

### Backend Setup

```bash
cd backend
python -m venv travelvenv

# Windows
travelvenv\Scripts\activate

# macOS / Linux
source travelvenv/bin/activate

pip install -r requirements.txt
cp .env.example .env   # fill in OPENTRIPMAP_API_KEY for live data
uvicorn app.main:app --reload --port 8000
```

API base URL: [http://localhost:8000/api/v1](http://localhost:8000/api/v1)
Health check: [http://localhost:8000/health](http://localhost:8000/health)
Auto-generated docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### Running Tests

```bash
cd backend
pytest
```

## Frontend Scripts

| Command | Description |
|---|---|
| `npm run dev` | Start Vite dev server (port 5173) |
| `npm run build` | Production build to `dist/` |
| `npm run preview` | Preview production build locally |

## Environment Variables

### Frontend

| Variable | Location | Default | Description |
|---|---|---|---|
| `VITE_API_BASE_URL` | `frontend/.env` | `http://localhost:8000/api/v1` | Backend API base URL |

### Backend

| Variable | Location | Default | Description |
|---|---|---|---|
| `ENVIRONMENT` | `backend/.env` | `development` | Application environment |
| `API_HOST` | `backend/.env` | `0.0.0.0` | Server host |
| `API_PORT` | `backend/.env` | `8000` | Server port |
| `CORS_ORIGINS` | `backend/.env` | `http://localhost:5173,http://localhost:3000` | Allowed CORS origins |
| `OPENTRIPMAP_API_KEY` | `backend/.env` | `""` | OpenTripMap API key (required for attractions/hotels/restaurants) |

Copy `frontend/.env.example` to `frontend/.env` and `backend/.env.example` to `backend/.env` to override defaults.

## Backend API Endpoints

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

## Current Milestone Status

| Milestone | Status |
|---|---|
| Frontend Implementation | **Complete** |
| Frontend Review & Refactoring | **Complete** |
| Backend Implementation | **Complete** |
| API Integration | **Complete** |
| Deployment | Planned |

## Screenshots

> Screenshots will be added after visual QA and deployment.

## Future Roadmap

| Phase | Focus |
|---|---|
| Phase 1 (MVP) | Frontend + Backend + Deployment |
| Phase 2 | Database integration |
| Phase 3 | Authentication and user accounts |
| Phase 4 | AI-powered itinerary generation |
| Phase 5 | Personalization and saved trips |

## Documentation

All specs live in `Docs/`:

- `PROJECT_CONTEXT.md` — project goals and constraints
- `PRD_v1.1.md` — product requirements
- `software_architecture.md` — system architecture
- `ui_design.md` — UI/UX design guide
- `component_library.md` — component specifications
- `api_specification.md` — REST API contract
- `project_structure.md` — folder structure blueprint
- `prompt_playbook.md` — prompt engineering log
