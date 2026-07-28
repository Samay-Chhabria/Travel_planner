# Travel Planner MVP - Project Requirements Document (PRD)

**Version:** 1.1

## Purpose

This document is the single source of truth for the project. It provides
consistent context for AI coding assistants (Cursor, GitHub Copilot,
ChatGPT, Claude, Gemini, etc.). Every feature will be built
incrementally using prompt engineering.

------------------------------------------------------------------------

# Project Vision

Build a **modern, Airbnb-inspired Travel Planner** with a beautiful
frontend and a clean FastAPI backend that aggregates free travel APIs.

This is **Phase 1 (MVP)**.

The application should be fully functional, deployable, and
portfolio-ready without requiring AI features, authentication, or a
database.

Future phases will add AI, authentication, and persistent storage
without changing the core architecture.

------------------------------------------------------------------------

# Primary Objectives

-   Learn prompt engineering through real software development.
-   Build a professional portfolio project.
-   Create a polished, responsive UI.
-   Build a modular FastAPI backend.
-   Integrate multiple free travel APIs.
-   Deploy the application.

------------------------------------------------------------------------

# Current Scope (Phase 1)

## Included

-   React + Vite frontend
-   Tailwind CSS
-   FastAPI backend
-   API aggregation layer
-   Modern responsive UI
-   Travel destination search
-   Weather
-   Attractions
-   Restaurants
-   Hotels
-   Maps
-   Trip planner (rule-based)
-   Deployment

## Deferred

-   AI itinerary generation
-   Authentication
-   Database
-   Saved trips
-   User profiles
-   Payments

------------------------------------------------------------------------

# UI Direction

**Design Inspiration:** Airbnb

Principles: - Clean - Modern - Spacious - Card-based - Mobile-first -
Accessible - Consistent

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

## External APIs

-   Open-Meteo
-   Nominatim
-   OpenTripMap

## Deployment

-   Frontend: Vercel
-   Backend: Render

------------------------------------------------------------------------

# Pages

## Implementation Status: Frontend & Backend Complete

1.  Landing Page — **Implemented**
2.  Destination Search — **Implemented**
3.  Destination Details — **Implemented**
4.  Trip Planner — **Implemented**
5.  About — **Implemented**
6.  Contact — **Implemented**

------------------------------------------------------------------------

# Backend Responsibilities

-   Never expose third-party APIs directly to the frontend.
-   Validate requests.
-   Handle errors consistently.
-   Aggregate external API responses.
-   Keep endpoints RESTful.

------------------------------------------------------------------------

# Development Workflow

For every feature:

1.  Understand requirements.
2.  Design the solution.
3.  Write the prompt.
4.  Generate code.
5.  Review AI output.
6.  Improve the prompt.
7.  Integrate.
8.  Test.
9.  Refactor.

------------------------------------------------------------------------

# Prompt Engineering Rules

Every implementation prompt should contain:

-   Role
-   Context
-   Task
-   Requirements
-   Constraints
-   Output Format

Never ask an AI to build the whole application in one prompt.

------------------------------------------------------------------------

# AI Collaboration Rules

The AI should:

-   Explain architecture before writing code.
-   Preserve project structure.
-   Build one feature at a time.
-   Never rewrite unrelated files.
-   Generate production-quality code.
-   Keep frontend and backend decoupled.
-   Prefer free/open-source tools.
-   Ask questions when requirements are ambiguous.

------------------------------------------------------------------------

# Roadmap

## Phase 1

-   UI Design
-   Frontend
-   Backend
-   API Integration
-   Deployment

## Phase 2

-   Database

## Phase 3

-   Authentication

## Phase 4

-   AI Features

## Phase 5

-   Personalization & Saved Trips

------------------------------------------------------------------------

# Definition of Success

A deployed Travel Planner that demonstrates: - Excellent UI/UX - Clean
React architecture - Modular FastAPI backend - Multiple API
integrations - Professional prompt engineering workflow
