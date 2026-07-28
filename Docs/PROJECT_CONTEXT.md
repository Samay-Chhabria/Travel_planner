# PROJECT_CONTEXT.md

# Travel Planner - AI Project Context

> This file is the permanent context for every AI coding assistant
> working on this project. Read this document before responding to any
> implementation request.

------------------------------------------------------------------------

# Project Goal

Build a **modern, Airbnb-inspired Travel Planner** as a professional
portfolio project.

The project is also a **Prompt Engineering learning project**. The
objective is not only to build the application but to learn how to
collaborate effectively with AI throughout the software development
lifecycle.

------------------------------------------------------------------------

# Current Phase

**Phase 1 - MVP**

## Milestone Status

-   Frontend Implementation: **Complete**
-   Frontend Review and Refactoring: **Complete**
-   Backend Implementation: **Complete**
-   API Integration: **Complete**
-   Deployment: Not started

The MVP focuses on:

-   Beautiful, responsive frontend
-   Clean FastAPI backend
-   Integration with free travel APIs
-   Deployment

Do NOT introduce AI features, authentication, databases, payments, or
unnecessary complexity unless explicitly requested.

------------------------------------------------------------------------

# Tech Stack

## Frontend

-   React
-   Vite
-   Tailwind CSS
-   React Router
-   Axios

## Backend

-   FastAPI
-   Pydantic
-   Uvicorn
-   httpx

## Deployment

-   Frontend: Vercel
-   Backend: Render

------------------------------------------------------------------------

# Design Philosophy

The UI should be inspired by Airbnb.

Characteristics:

-   Modern
-   Clean
-   Spacious
-   Professional
-   Card-based
-   Responsive
-   Accessible
-   Consistent

Never create outdated-looking interfaces.

------------------------------------------------------------------------

# Development Philosophy

Build one feature at a time.

Never generate the entire project at once.

Every feature should be modular, reusable, and production-ready.

Always preserve the existing architecture.

------------------------------------------------------------------------

# Backend Responsibilities

The backend is an API gateway.

Responsibilities include:

-   Calling external APIs
-   Validating requests
-   Normalizing API responses
-   Returning clean JSON to the frontend
-   Handling errors consistently

The frontend should never communicate directly with third-party APIs
unless explicitly instructed.

------------------------------------------------------------------------

# Free APIs (Preferred)

-   Open-Meteo
-   Nominatim
-   OpenTripMap

Prefer free services.

Avoid paid APIs unless requested.

------------------------------------------------------------------------

# Coding Standards

-   Clean Architecture
-   Modular code
-   Reusable components
-   Small focused files
-   Meaningful naming
-   No duplicated logic
-   Follow React and FastAPI best practices
-   Explain architectural decisions when appropriate

------------------------------------------------------------------------

# AI Collaboration Rules

When asked to build a feature:

1.  Read this context.
2.  Build ONLY the requested feature.
3.  Do not modify unrelated files.
4.  Reuse existing components whenever possible.
5.  Ask questions if requirements are ambiguous.
6.  Explain the implementation approach before generating code.
7.  Generate complete files when requested.
8.  Keep code production-ready.

------------------------------------------------------------------------

# Prompt Engineering Rules

Assume feature prompts will contain:

-   Role
-   Context
-   Task
-   Requirements
-   Constraints
-   Output Format

Follow those instructions while using this document as the project's
long-term context.

------------------------------------------------------------------------

# Current Scope

Included: - Landing Page - Destination Search - Destination Details -
Trip Planner - Weather - Maps - Hotels - Restaurants - Attractions -
Responsive UI - Backend API integration - Deployment

Not included (yet): - AI itinerary generation - Authentication -
Database - Saved trips - User profiles - Payments

------------------------------------------------------------------------

# Expected Folder Structure

travel-planner/ ├── frontend/ ├── backend/ └── docs/

------------------------------------------------------------------------

# Workflow

For every feature:

1.  Understand the request.
2.  Design the solution.
3.  Explain the architecture.
4.  Generate code.
5.  Review.
6.  Refactor if necessary.

Never skip directly to coding without understanding the requested
feature.

------------------------------------------------------------------------

# Important

This document defines the project's long-term direction.

If a user prompt conflicts with this document, ask for clarification
before making architectural changes.

Always optimize for: - Maintainability - Readability - Scalability -
Reusability - Consistency
