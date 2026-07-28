# Project Structure Blueprint - Travel Planner

## 1. Purpose

This document defines the complete folder structure for the Travel Planner MVP based on the PRD, project context, software architecture, UI/UX design, component library, and API specification.

The structure is intended to support:
- a clean React + Vite frontend
- a modular FastAPI backend
- decoupled frontend and backend concerns
- scalable future growth without major restructuring
- clear separation between UI, API, business logic, and integrations

---

## 2. Overall Repository Structure

```text
travel-planner/
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/
│   │   ├── components/
│   │   ├── data/
│   │   ├── hooks/
│   │   ├── layouts/
│   │   ├── pages/
│   │   ├── routes/
│   │   ├── services/
│   │   ├── styles/
│   │   ├── utils/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── .env.example
│   ├── package.json
│   ├── postcss.config.js
│   ├── tailwind.config.js
│   ├── vite.config.js
│   └── index.html
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   └── routes/
│   │   ├── core/
│   │   ├── integrations/
│   │   │   └── providers/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   └── main.py
│   ├── requirements.txt
│   └── README.md
├── Docs/
│   ├── PROJECT_CONTEXT.md
│   ├── PRD_v1.1.md
│   ├── software_architecture.md
│   ├── ui_design.md
│   ├── component_library.md
│   ├── api_specification.md
│   ├── project_structure.md
│   └── prompt_playbook.md
├── .env.example
├── .gitignore
├── vercel.json
├── render.yaml
└── README.md
```

---

## 3. Folder and File Purpose

## 3.1 Root Level

### travel-planner/
Purpose: the top-level project container that groups the frontend, backend, and documentation.

### README.md
Purpose: repository overview, setup summary, project description, and high-level usage instructions.

### .env.example
Purpose: reference for all environment variables across frontend and backend.

### .gitignore
Purpose: excludes dependencies, build output, environment files, and IDE artifacts from version control.

### vercel.json
Purpose: Vercel deployment configuration for the frontend (build command, output directory, SPA rewrites).

### render.yaml
Purpose: Render deployment configuration for the backend (runtime, build, start command, environment variables).

---

## 3.2 Frontend Root

### frontend/
Purpose: contains everything related to the React + Vite user interface.

### frontend/public/
Purpose: stores static assets that are served directly by the app.

#### Contents
- favicon.ico
- logo.svg
- robots.txt

### frontend/package.json
Purpose: defines frontend dependencies, scripts, and project metadata.

### frontend/vite.config.js
Purpose: Vite configuration for development, build, and environment handling.

### frontend/tailwind.config.js
Purpose: Tailwind CSS configuration with custom design tokens for colors, shadows, border-radius, spacing, and typography.

### frontend/postcss.config.js
Purpose: PostCSS configuration for Tailwind CSS processing.

### frontend/index.html
Purpose: the main HTML entry file for the Vite app.

### frontend/.env.example
Purpose: frontend-specific environment variable reference (VITE_API_BASE_URL).

---

## 3.3 Frontend Source Structure

### frontend/src/
Purpose: the main application source folder for all React UI code.

### frontend/src/main.jsx
Purpose: application bootstrap file that mounts React into the DOM.

### frontend/src/App.jsx
Purpose: root application component that wires routes and global layout.

---

## 3.4 Frontend Assets

### frontend/src/assets/
Purpose: stores local images, icons, fonts, and other static frontend assets.

#### Subfolders
- images/
- icons/
- illustrations/

---

## 3.5 Frontend Components

### frontend/src/components/
Purpose: contains reusable UI components organized by domain.

#### Implemented Subfolders and Components

##### common/
Shared primitive UI components used across multiple pages.
- `Button.jsx` — primary/secondary/ghost/link button variants
- `Badge.jsx` — accent/highlight/primary/neutral variants
- `Input.jsx` — text input with label, error, and icon support (reused in Contact page)
- `StarRating.jsx` — 5-star display with filled/half/empty states
- `PriceLevel.jsx` — price level indicator ($, $$, $$$, $$$$)
- `SectionHeader.jsx` — eyebrow + heading + description pattern
- `DetailCard.jsx` — reusable card for attractions, restaurants, hotels

##### layout/
Structural components that define page scaffolding.
- `Navbar.jsx` — sticky top navigation with mobile menu, active states, skip-to-content link
- `Footer.jsx` — site footer with brand, navigation, and links
- `PageContainer.jsx` — centered max-width content wrapper
- `SectionWrapper.jsx` — section-level spacing and background helper

##### cards/
High-level card components for specific content types.
- `DestinationCard.jsx` — destination preview card with image, name, region
- `ThemeCard.jsx` — travel theme card with overlay and tag
- `TestimonialCard.jsx` — user testimonial with quote, avatar, attribution

##### search/
Components for the Explore page search and filter experience.
- `SearchBar.jsx` — search input with icon and size variants
- `FilterBar.jsx` — travel type and region filter controls
- `SortSelect.jsx` — sort order dropdown
- `ViewToggle.jsx` — grid/list view toggle

##### destination/
Components for the Destination Details page.
- `DestinationHero.jsx` — hero banner with image, name, region, highlights
- `OverviewSection.jsx` — description, highlights badges, quick info sidebar
- `WeatherWidget.jsx` — current conditions and forecast via backend weather API
- `AttractionsSection.jsx` — destination-specific attraction cards
- `RestaurantsSection.jsx` — destination-specific restaurant cards
- `HotelsSection.jsx` — destination-specific hotel cards
- `MapPlaceholder.jsx` — placeholder for future interactive map
- `PlanTripCTA.jsx` — call-to-action to start planning

##### planner/
Components for the Trip Planner page.
- `DestinationSelector.jsx` — searchable destination picker with grid
- `DatePicker.jsx` — start/end date selection
- `BudgetSelector.jsx` — budget level picker (budget/moderate/luxury)
- `TravelersSelector.jsx` — group size selector
- `ThemeSelector.jsx` — travel theme grid with images
- `TripSummary.jsx` — live sidebar summary of selected options
- `ItineraryPlaceholder.jsx` — generated day-by-day itinerary display

##### contact/
Components for the Contact page.
- `ContactForm.jsx` — name/email/message form with validation (no submission)
- `ContactInfo.jsx` — contact details and location info
- `FAQSection.jsx` — expandable FAQ accordion
- `SocialLinks.jsx` — social media link buttons

##### about/
Components for the About page.
- `HeroSection.jsx` — about page hero
- `MissionSection.jsx` — mission and values
- `FeaturesSection.jsx` — key features grid
- `TechStackSection.jsx` — technologies used
- `TeamSection.jsx` — developer information

##### sections/
Landing page section components.
- `HeroSection.jsx` — main hero with search bar
- `FeaturedDestinations.jsx` — featured destination card grid
- `PopularThemes.jsx` — travel theme card grid
- `TestimonialsSection.jsx` — user testimonial carousel

##### feedback/
State components for loading, empty, and error conditions.
- `EmptyState.jsx` — friendly message with optional action
- `ErrorState.jsx` — error message with retry option
- `LoadingState.jsx` — skeleton loaders for cards and grids

##### forms/
Reserved for future form-specific components.

---

## 3.6 Frontend Pages

### frontend/src/pages/
Purpose: contains route-level page components for each major user journey.

#### Implemented Pages
- `HomePage.jsx` — Landing page (Hero, Featured, Themes, Testimonials)
- `ExplorePage.jsx` — Destination search with filters, sort, view toggle
- `DestinationDetailsPage.jsx` — Full destination details with all sections
- `TripPlannerPage.jsx` — Trip planning form with itinerary generation
- `AboutPage.jsx` — Brand story, mission, features, tech stack, team
- `ContactPage.jsx` — Contact form, info, FAQ, social links
- `NotFoundPage.jsx` — 404 page

---

## 3.7 Frontend Routes

### frontend/src/routes/
Purpose: stores route definitions and route configuration.

#### Files
- `routes.jsx` — all route definitions with React.lazy code splitting and Suspense fallbacks

---

## 3.8 Frontend Services

### frontend/src/services/
Purpose: contains frontend API client logic used to call the backend.

#### Files
- `apiClient.js` — Axios instance with base URL, request/response interceptors, and error normalization
- `destinationService.js` — getFeaturedDestinations, searchDestinations, getDestinationById
- `weatherService.js` — getWeatherForDestination
- `attractionsService.js` — getAttractionsForDestination
- `restaurantsService.js` — getRestaurantsForDestination
- `hotelsService.js` — getHotelsForDestination
- `plannerService.js` — generateTripPlan

> **Note:** `contactService.js` was removed during the production readiness review (stub that threw an error, was never imported by any component).

---

## 3.9 Frontend Hooks

### frontend/src/hooks/
Purpose: contains reusable React hooks for UI logic and data fetching.

#### Files
- `useDebounce.js` — debounced value for search input
- `useFetch.js` — generic data fetching hook with loading/error states

---

## 3.10 Frontend Utilities

### frontend/src/utils/
Purpose: stores reusable helper functions and small utilities.

#### Files
- `constants.js` — 20 destinations (fallback data), 6 travel themes, API base URL, testimonials
- `validators.js` — contact form validation (validateContactForm, hasErrors)
- `dateUtils.js` — date helpers (daysBetween, formatDateRange)

---

## 3.11 Frontend Data

### frontend/src/data/
Purpose: stores static data files used by components.

> **Note:** The `data/` directory and `attractionsData.js` were removed during the production readiness review as dead code (no longer imported after API integration).

---

## 3.12 Frontend Styles

### frontend/src/styles/
Purpose: centralizes styling-related files, tokens, and global appearance rules.

#### Files
- `tailwind.css` — Tailwind CSS imports and directives (main entry)
- `variables.css` — CSS custom properties (color tokens, spacing, shadows)

> **Note:** `globals.css` was removed during the production readiness review (contained only a comment, was never imported).

---

## 3.13 Frontend Layouts

### frontend/src/layouts/
Purpose: contains shared page-layout structures.

#### Files
- `MainLayout.jsx` — app shell with Navbar, main content area, and Footer

> **Note:** `PageLayout.jsx` was removed during the production readiness review (empty placeholder, was never imported).

---

## 3.14 Backend Root

### backend/
Purpose: contains everything related to the FastAPI backend service.

### backend/requirements.txt
Purpose: lists backend Python dependencies.

### backend/.env.example
Purpose: backend-specific environment variable template (ENVIRONMENT, API_HOST, API_PORT, CORS_ORIGINS, OPENTRIPMAP_API_KEY).

### backend/pyproject.toml
Purpose: pytest configuration (asyncio_mode, test paths).

### backend/README.md
Purpose: backend setup instructions, API endpoints overview, and local run guidance.

---

## 3.15 Backend Application

### backend/app/
Purpose: contains the FastAPI application source.

### backend/app/main.py
Purpose: the main FastAPI entrypoint that wires routes, middleware, and app initialization.

---

## 3.16 Backend API Layer

### backend/app/api/routes/
Purpose: stores route modules grouped by domain.

#### Files
- `health.py`
- `destinations.py`
- `geocoding.py`
- `weather.py`
- `attractions.py`
- `restaurants.py`
- `hotels.py`
- `trip_planner.py`

---

## 3.17 Backend Core

### backend/app/core/
Purpose: contains shared application configuration and core infrastructure.

#### Files
- `config.py`
- `exceptions.py`
- `logging.py`
- `middleware.py`

---

## 3.18 Backend Schemas

### backend/app/schemas/
Purpose: defines request and response models using Pydantic.

#### Files
- `destination.py`
- `weather.py`
- `attraction.py`
- `restaurant.py`
- `hotel.py`
- `trip_plan.py`
- `common.py`
- `geocoding.py`

---

## 3.19 Backend Services

### backend/app/services/
Purpose: holds orchestration logic for business flows and provider aggregation.

#### Files
- `destination_service.py`
- `weather_service.py`
- `geocoding_service.py`
- `attraction_service.py`
- `restaurant_service.py`
- `hotel_service.py`
- `trip_planner_service.py`

---

## 3.20 Backend Integrations

### backend/app/integrations/providers/
Purpose: contains adapter code and provider-specific integration modules.

#### Files
- `open_meteo_client.py`
- `nominatim_client.py`
- `open_trip_map_client.py`

---

## 3.21 Backend Utilities

### backend/app/utils/
Purpose: stores shared helper functions for backend processing.

#### Files
- `http_utils.py`
- `response_utils.py`
- `converters.py`

---

## 3.22 Tests

### backend/tests/
Purpose: contains the pytest test suite for all backend modules.

#### Files
- `conftest.py` — shared test fixtures (httpx AsyncClient)
- `test_destination.py` / `test_destination_api.py` — destination unit and API tests
- `test_weather.py` / `test_weather_api.py` — weather unit and API tests
- `test_geocoding.py` / `test_geocoding_api.py` — geocoding unit and API tests
- `test_attraction.py` / `test_attraction_api.py` — attraction unit and API tests
- `test_restaurant.py` / `test_restaurant_api.py` — restaurant unit and API tests
- `test_hotel.py` / `test_hotel_api.py` — hotel unit and API tests
- `test_trip_planner.py` / `test_trip_planner_api.py` — trip planner unit and API tests

---

## 3.23 Documentation Folder

### Docs/
Purpose: contains all product, design, architecture, planning, and specification artifacts.

#### Files
- `PROJECT_CONTEXT.md` — project goals, constraints, and AI collaboration rules
- `PRD_v1.1.md` — product requirements document
- `software_architecture.md` — system architecture specification
- `ui_design.md` — UI/UX design guide
- `component_library.md` — component specifications and design system
- `api_specification.md` — REST API contract
- `project_structure.md` — this file (folder structure blueprint)
- `prompt_playbook.md` — prompt engineering log for all development phases

---

## 4. Implementation Order

The project has been implemented in this order:

1. Frontend shell and routing
2. Shared layout and design-system foundation
3. Landing page and core navigation
4. Destination search experience
5. Destination details experience
6. Trip planner experience
7. About and contact pages
8. Frontend review and refactoring
9. Backend health and destination endpoints
10. Weather, attractions, restaurants, and hotels endpoints
11. Trip planner endpoint
12. Deployment configuration (planned)

---

## 5. Notes on Scope and Extensibility

This structure is intentionally aligned with the MVP and future phases.

It supports:
- current travel discovery and planning features
- later addition of authentication and user accounts
- future AI-based itinerary generation
- future persistence and saved-trip functionality

The structure remains modular enough that new features can be added without major refactoring.
