# Software Architecture - Travel Planner

## 1. Purpose

This document defines the software architecture for the Travel Planner MVP. It is aligned with the project context and PRD and covers the system structure, responsibilities, integrations, deployment approach, and technical constraints for the initial release.

## 2. Project Context Summary

The Travel Planner is a modern, Airbnb-inspired travel planning website built as a portfolio project and a prompt engineering learning exercise. The MVP focuses on:

- Beautiful and responsive frontend experience
- Clean FastAPI backend
- Integration with free travel APIs
- Deployment readiness

The system does not include authentication, databases, payments, or AI-based itinerary generation in the MVP.

## 3. Architectural Goals

The architecture is designed to be:

- Modular and maintainable
- Easy to extend in later phases
- Frontend and backend decoupled
- Production-ready for MVP deployment
- Consistent with React + Vite + Tailwind + FastAPI standards

## 4. High-Level Architecture

The system follows a client-server architecture with a thin backend gateway pattern.

### 4.1 Overview

- The user interacts with a React-based frontend.
- The frontend sends requests to a FastAPI backend.
- The backend acts as a gateway to third-party travel APIs.
- The backend validates, aggregates, transforms, and returns normalized JSON responses.
- The frontend renders the data in a polished, card-based UI.

### 4.2 High-Level Flow

1. User opens the site and browses travel content.
2. User searches for a destination or plans a trip.
3. Frontend sends a request to the backend.
4. Backend calls one or more external APIs.
5. Backend normalizes and validates the data.
6. Frontend renders the response in pages and components.

## 5. System Components

### 5.1 Frontend Application

The frontend is a single-page application built with React and Vite.

Responsibilities:
- Render pages and UI components
- Manage user interaction and navigation
- Send requests to the backend API
- Display destinations, weather, attractions, restaurants, hotels, maps, and trip planning content
- Handle loading, empty, and error states gracefully

### 5.2 Backend API Layer

The backend is a FastAPI application that serves as the business-facing API layer.

Responsibilities:
- Receive requests from the frontend
- Validate inputs using Pydantic models
- Call external travel APIs
- Normalize third-party responses
- Return clean and predictable JSON to the frontend
- Handle errors consistently

### 5.3 External API Integration Layer

The backend integrates with free travel and mapping services through dedicated adapters.

Responsibilities:
- Isolate third-party API logic from the main application
- Simplify provider switching in the future
- Standardize data transformation
- Improve resilience and maintainability

## 6. Architectural Style

The architecture follows a layered approach:

- Presentation Layer: React pages and UI components
- Application Layer: frontend routing, request handling, API client logic
- API Layer: FastAPI endpoints
- Service Layer: backend business logic and provider orchestration
- Integration Layer: adapters for external services
- Data Models: Pydantic schemas and normalized response structures

## 7. Frontend Architecture

### 7.1 Technology Stack

- React
- Vite
- Tailwind CSS
- React Router
- Axios

### 7.2 Frontend Structure

Suggested structure:

- src/
  - pages/
  - components/
  - services/
  - hooks/
  - utils/
  - styles/
  - routes/

### 7.3 Frontend Modules

#### Pages
- Landing Page
- Destination Search
- Destination Details
- Trip Planner
- About
- Contact

#### Reusable UI Components
- Navbar
- Hero section
- Search bar
- Destination cards
- Travel detail cards
- Weather widget
- Map container
- Trip planner form
- Empty/error/loading states
- Footer

### 7.4 Frontend State Strategy

The architecture should use a simple and lightweight state approach:

- Local component state for form input and UI state
- Shared state only where needed across routes or components
- No database-backed user state in MVP
- No complex global state management unless the UI grows beyond the MVP scope

### 7.5 Frontend API Communication

The frontend should not directly call third-party APIs. It should communicate only with the backend API.

Responsibilities of the frontend API layer:
- Submit requests to backend endpoints
- Handle success and error responses
- Centralize endpoint definitions
- Keep UI code clean and decoupled from backend implementation details

## 8. Backend Architecture

### 8.1 Technology Stack

- FastAPI
- Pydantic
- Uvicorn
- httpx

### 8.2 Backend Structure

Suggested structure:

- app/
  - main.py
  - api/
    - routes/
  - schemas/
  - services/
  - integrations/
  - core/
  - utils/

### 8.3 Backend Modules

#### API Routes
Routes should be organized by concern:
- Destination routes
- Weather routes
- Attractions routes
- Restaurants routes
- Hotels routes
- Trip planning routes
- Health/status routes

#### Services
Services handle orchestration and business logic:
- Destination service
- Weather service
- Geocoding service
- Attraction service
- Restaurant service
- Hotel service
- Trip planning service

#### Schemas
Pydantic schemas should define:
- Request payloads
- Response payloads
- Validation rules
- Error response contracts

### 8.4 Backend Design Principles

- Keep endpoints simple and RESTful
- Separate routing from business logic
- Keep integration logic isolated from API routes
- Normalize all third-party responses into a common structure
- Return consistent JSON payloads to the frontend

## 9. API Design

### 9.1 Backend API Responsibilities

The backend should expose endpoints such as:
- Search destinations
- Get destination details
- Get weather for a destination
- Get attractions near a destination
- Get restaurants near a destination
- Get hotel suggestions
- Generate a rule-based travel plan

### 9.2 Response Contract Strategy

The backend should provide a stable response structure so the frontend can render consistently.

Recommended principles:
- Use predictable field names
- Return meaningful status messages
- Return standardized error objects
- Keep response shapes consistent across modules

### 9.3 Error Handling Strategy

The backend should implement centralized error handling for:
- Invalid input
- Missing required parameters
- External API failures
- Timeout errors
- Unavailable providers

Errors should be reported in a predictable way and surfaced clearly in the frontend.

## 10. External API Integration Architecture

### 10.1 Preferred Providers

The architecture supports free and open travel data providers:
- Open-Meteo (weather)
- Nominatim (geocoding)
- OpenTripMap (attractions, hotels, restaurants)

### 10.2 Integration Pattern

Each external provider should be wrapped in a dedicated adapter or service.

Example approach:
- A provider adapter handles API requests and response parsing
- A normalization layer transforms the provider data into the application’s internal schema
- The main service composes data from one or more providers

### 10.3 Benefits of This Pattern

- Prevents backend code from becoming tightly coupled to third-party APIs
- Makes future provider changes low risk
- Improves testability
- Keeps the frontend independent from provider-specific data formats

## 11. Data Flow Architecture

### 11.1 Destination Search Flow

1. User enters a destination query in the frontend.
2. Frontend sends a request to the backend search endpoint.
3. Backend validates the input.
4. Backend calls a geocoding or destination provider.
5. Backend normalizes the result.
6. Frontend displays destination suggestions or details.

### 11.2 Details and Planning Flow

1. User opens a destination detail page.
2. Frontend requests weather, attractions, restaurants, and hotels from the backend.
3. Backend orchestrates one or more provider calls.
4. Backend merges and normalizes the data.
5. Frontend renders all sections on the page.

### 11.3 Trip Planner Flow

1. User provides trip preferences, dates, and destination information.
2. Frontend sends planner data to the backend.
3. Backend uses a rule-based logic layer to create an itinerary-like plan.
4. Backend returns a structured plan to the frontend.
5. Frontend displays the itinerary in a clear format.

## 12. Deployment Architecture

### 12.1 Frontend Deployment

- Deploy the Vite frontend to Vercel
- Use a production build optimized for static hosting
- Serve the application over HTTPS

### 12.2 Backend Deployment

- Deploy the FastAPI backend to Render
- Run with Uvicorn in a production environment
- Expose a public API endpoint for frontend consumption

### 12.3 Environment Configuration

The application should use environment variables for:
- API base URLs
- External provider keys if ever required
- Frontend and backend environment settings
- Deployment-specific configuration

## 13. Security Architecture

Because this is an MVP, security should stay simple but sensible.

### 13.1 Principles

- Do not expose third-party API secrets to the frontend
- Validate all inputs on the backend
- Restrict cross-origin requests appropriately
- Use HTTPS in production
- Keep secrets in environment variables

### 13.2 MVP Security Scope

The MVP does not require authentication or user accounts, so the security model remains lightweight.

## 14. Reliability and Resilience

### 14.1 Reliability Goals

- Graceful handling of third-party API unavailability
- Clear loading and error states in the UI
- Timeouts for external requests
- Consistent error responses from the backend

### 14.2 Resilience Patterns

- Retry logic for transient failures where appropriate
- Fallback behavior when a provider is unavailable
- Defensive frontend rendering for partial data failures
- Logging for backend failures and response issues

## 15. Observability and Maintainability

### 15.1 Logging

The backend should log:
- Request start and completion
- External API failures
- Validation issues
- Unexpected exceptions

### 15.2 Maintainability Practices

- Keep files small and focused
- Separate UI, API, and service responsibilities
- Reuse common components and shared logic
- Avoid duplication across API integration modules

## 16. Testing Strategy

The project includes a comprehensive pytest test suite covering unit tests and API endpoint tests for all backend modules.

### 16.1 Backend Testing
- Unit tests for validation and normalization logic
- Service tests for provider orchestration
- Endpoint tests for request/response behavior using httpx AsyncClient with ASGITransport

### 16.2 Test Framework
- pytest with pytest-asyncio
- AsyncClient with ASGITransport for endpoint testing
- Mocked external API calls for deterministic tests

## 17. Repository Structure

The repository is organized as follows:

- frontend/
  - src/
    - pages/
    - components/
    - services/
    - hooks/
    - utils/
    - routes/
    - styles/
    - layouts/
- backend/
  - app/
    - api/routes/
    - services/
    - integrations/providers/
    - schemas/
    - core/
    - utils/
    - main.py
  - tests/
  - .env.example
  - pyproject.toml
  - requirements.txt
- Docs/

## 18. Extensibility Plan

The architecture is intentionally designed to support future phases without major restructuring.

### Phase 2 and Beyond
- Add a database layer when persistent data becomes necessary
- Introduce authentication and user profiles later
- Add AI-based itinerary generation in a separate service layer
- Expand the backend without changing the frontend contract unnecessarily

## 19. Architectural Decisions Summary

Key decisions for this MVP:

- React + Vite for the frontend
- FastAPI for the backend API layer
- Backend as an API gateway to external travel providers
- No database in MVP
- No authentication in MVP
- Frontend consumes only backend endpoints
- Free and open travel APIs are preferred
- Vercel for frontend deployment and Render for backend deployment

## 20. Conclusion

The proposed architecture provides a scalable, modular, and deployment-ready foundation for the Travel Planner MVP. It keeps the system simple enough for an initial portfolio release while leaving room for future growth in later phases.
