# Component Library Plan - Travel Planner

## 1. Purpose

This document defines the complete component library for the Travel Planner MVP. It translates the product requirements, UX direction, and system architecture into a structured frontend component plan for implementation.

The component library is designed to support:
- A polished, Airbnb-inspired experience
- Responsive behavior across mobile, tablet, and desktop
- Consistent visual language
- Reusable UI building blocks
- A scalable frontend architecture for future growth

---

## 2. Product and UX Foundation

### 2.1 Core Experience Goals
- Make destination discovery effortless
- Reduce cognitive load
- Build trust through clarity
- Support trip planning without overwhelm

### 2.2 Visual Direction
- Calm, warm, premium, editorial
- Spacious layout with generous whitespace
- Modern card-based structure
- Soft nature-inspired accent colors
- Clear hierarchy and low clutter

### 2.3 Design Principles
- Simplicity first
- Spacious visual rhythm
- Confidence through structure
- Mobile-first thinking
- Calm, travel-inspired aesthetic

---

## 3. Design System Foundation

### 3.1 Color Tokens
- Background: #FAF7F2
- Surface: #FFFFFF
- Primary text: #222222
- Secondary text: #717171
- Accent: #2F6D6A
- Highlight: #F28C6B
- Border: #EDE5DA

### 3.2 Typography Scale
- Hero heading: 48–64px desktop, 32–40px mobile
- Section heading: 28–36px desktop, 22–28px mobile
- Body text: 16–18px
- Small labels: 12–14px

### 3.3 Spacing Scale
- 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px

### 3.4 Corner Radius
- Buttons: 999px or rounded pill style for primary actions
- Cards and containers: 16–20px

### 3.5 Shadow Style
- Soft, subtle elevation
- Minimal, airy, not heavy

---

## 4. Component Architecture Overview

The frontend should be built from a layered component structure:

1. Foundations
   - Color, typography, spacing, icons, motion
2. Primitive UI Components
   - Buttons, inputs, cards, badges, modals, loaders, alerts
3. Composite UI Components
   - Search bar, navbar, hero section, destination cards, planner form, summary card
4. Page-Level Sections
   - Landing page sections, destination details sections, planner experience, about/contact content blocks

---

## 5. Foundational Components

### 5.1 Button
**Purpose**
- Primary actions such as search, plan trip, explore, contact

**Variants**
- Primary
- Secondary
- Tertiary
- Icon button
- Ghost button

**States**
- Default
- Hover
- Focus
- Active
- Disabled
- Loading

**Behavior**
- Rounded, approachable, lightweight
- Primary button uses accent color
- Secondary button uses muted surface styling

**Accessibility**
- Visible focus ring
- Minimum touch target size for mobile
- Clear labels and semantic button usage

---

### 5.2 Input Field
**Purpose**
- Destination search, contact form, planner form fields

**Variants**
- Text input
- Search input
- Date input
- Select/dropdown
- Textarea

**States**
- Default
- Focused
- Filled
- Error
- Success

**Behavior**
- Large enough for touch interaction
- Rounded styling with soft border
- Clear placeholder text
- Inline validation feedback

**Accessibility**
- Proper labels
- Screen-reader support
- Visible validation messages

---

### 5.3 Icon Button
**Purpose**
- Compact actions such as filter toggle, menu, search, favorite, close

**Behavior**
- Minimal footprint
- Clear hover/focus feedback
- Consistent icon size and spacing

---

### 5.4 Badge / Tag
**Purpose**
- Label categories such as region, season, travel type, amenity

**Usage**
- Filter chips
- Highlights on cards
- Tag clusters in planner summary

---

### 5.5 Divider / Separator
**Purpose**
- Organize sections and create visual calmness

**Usage**
- Between page sections
- Between list items
- In forms and summary blocks

---

### 5.6 Loader / Skeleton
**Purpose**
- Indicate loading states for cards, search results, and detail sections

**Behavior**
- Soft pulse or shimmer style
- Match card structure to reduce perceived load

---

### 5.7 Alert / Inline Feedback
**Purpose**
- Show success, warning, and error messages

**Variants**
- Success
- Error
- Informational

**Usage**
- Form submission feedback
- API failure messages
- Empty-state guidance

---

## 6. Layout Components

### 6.1 Page Container
**Purpose**
- Standardize max-width and horizontal padding across pages

**Behavior**
- Centered content layout
- Responsive padding for mobile/tablet/desktop
- Supports section spacing rhythm

---

### 6.2 Section Wrapper
**Purpose**
- Group related content blocks and maintain vertical spacing

**Usage**
- Hero section
- Featured destinations
- Destination details sections
- Footer area

---

### 6.3 Grid System
**Purpose**
- Create structured content layouts

**Patterns**
- 1-column mobile
- 2-column tablet
- 3-column desktop for cards and feature blocks

---

### 6.4 Stack / Spacing Layout
**Purpose**
- Manage vertical and horizontal rhythm consistently

**Behavior**
- Supports content organization without overcrowding

---

## 7. Content and Surface Components

### 7.1 Card
**Purpose**
- Present destinations, attractions, restaurants, hotels, and trip suggestions in a clean, scannable format

**Structure**
- Image or visual area
- Title
- Short description or metadata
- Supporting tags or highlights
- Optional CTA

**Variants**
- Destination card
- Attraction card
- Restaurant card
- Hotel card
- Trip summary card
- Featured card

**States**
- Default
- Hover
- Selected
- Disabled

**Behavior**
- Rounded corners
- Soft shadow
- Consistent spacing
- Responsive resizing

---

### 7.2 Hero Banner
**Purpose**
- Introduce the product or a destination with strong visual impact

**Content**
- Large scenic image or background
- Headline
- Supporting description
- CTA

**Responsive Behavior**
- Single-column on mobile
- Stronger visual emphasis on desktop

---

### 7.3 Summary Card
**Purpose**
- Display important trip details such as destination, dates, preferences, and plan outcome

**Usage**
- Trip planner page
- Planner review sidebar
- Post-planning confirmation panel

---

### 7.4 Content Block
**Purpose**
- Display structured information in sections such as overview, weather, food, attractions, and hotels

**Behavior**
- Section title
- Short explanatory text
- Related cards or bullets
- Clear grouping

---

## 8. Navigation Components

### 8.1 Header / Navbar
**Purpose**
- Provide primary navigation and brand identity

**Contents**
- Brand/logo
- Navigation links: Home, Explore, Planner, About, Contact
- Primary call to action

**Behavior**
- Sticky on desktop
- Collapsible on mobile
- Active state visible for current page

**Responsive Behavior**
- Mobile uses compact menu with clear grouping

---

### 8.2 Mobile Menu
**Purpose**
- Present navigation items clearly on smaller screens

**Behavior**
- Slide-over or overlay pattern
- Easy to dismiss
- Touch-friendly target sizes

---

### 8.3 Breadcrumbs
**Purpose**
- Help users understand their location within the app

**Usage**
- Useful on detailed destination pages and planner steps

---

### 8.4 Footer
**Purpose**
- Provide secondary navigation and supporting context

**Contents**
- Brand text
- Contact links
- Helpful utility links

---

## 9. Search and Discovery Components

### 9.1 Search Bar
**Purpose**
- Core action for destination discovery

**Structure**
- Input field
- Search icon
- Optional filter button

**Behavior**
- Large and prominent
- Clear placeholder text
- Search-first interaction pattern

**States**
- Idle
- Active
- Loading
- Empty result
- Error

---

### 9.2 Filter Bar / Filter Chips
**Purpose**
- Narrow results in a lightweight way

**Usage**
- Destination search page
- Results refinement

**Behavior**
- Compact, easy to tap
- Clear active/inactive states

---

### 9.3 Results List
**Purpose**
- Display a list of matching destinations or travel entities

**Behavior**
- Card-based layout
- Support empty, loading, and error states

---

## 10. Destination Experience Components

### 10.1 Destination Hero
**Purpose**
- Introduce a specific destination with imagery and summary information

**Contents**
- Image/banner
- Name
- Region or country
- Short description
- Key highlights

---

### 10.2 Destination Summary Card
**Purpose**
- Show high-level destination facts quickly

**Suggested Information**
- Best time to visit
- Region
- Currency or travel notes
- Quick highlights

---

### 10.3 Weather Widget
**Purpose**
- Present weather context for the destination

**Content**
- Current conditions
- Temperature
- Forecast summary

**Behavior**
- Clear, compact, and visually calm

---

### 10.4 Attractions Section
**Purpose**
- Show notable attractions in card form

**Behavior**
- Grid or horizontal scrolling on smaller devices

---

### 10.5 Restaurants Section
**Purpose**
- Present dining options in a structured card layout

---

### 10.6 Hotels Section
**Purpose**
- Display recommended stays or lodging suggestions

---

### 10.7 Map Container
**Purpose**
- Provide location context for the destination

**Behavior**
- Lightweight, informative, and non-dominant
- Works well with weather and attraction content

---

## 11. Trip Planner Components

### 11.1 Planner Form
**Purpose**
- Collect destination, dates, travel preferences, and trip constraints

**Fields**
- Destination
- Travel dates
- Duration
- Budget preference
- Trip style or interests
- Group size or traveler type

**Behavior**
- Minimal form fields
- Clear labels and helpful prompts
- Structured stepwise experience

---

### 11.2 Planner Step Indicator
**Purpose**
- Show progress through the planning flow

**Behavior**
- Clear, simple, and calm
- Works well on desktop and mobile

---

### 11.3 Planner Summary Panel
**Purpose**
- Show a live overview of selected trip details

**Contents**
- Destination
- Date range
- Preferences
- Suggested plan structure

---

### 11.4 Plan Recommendation Card
**Purpose**
- Present the output of the rule-based planner

**Contents**
- Suggested day-by-day structure
- Highlighted activities
- Travel pacing suggestions

---

## 12. Form Components

### 12.1 Contact Form
**Purpose**
- Enable simple contact submission

**Fields**
- Name
- Email
- Message

**Behavior**
- Friendly validation states
- Clear success and error states

---

### 12.2 Form Section Wrapper
**Purpose**
- Group form fields in a calm and readable layout

**Behavior**
- Consistent spacing and labels
- Good mobile stacking

---

## 13. Empty, Loading, and Error States

### 13.1 Empty State
**Purpose**
- Guide users when no content is available

**Examples**
- No search results
- No attractions found
- No planner results yet

**Content**
- Friendly message
- Brief explanation
- Optional next-step CTA

---

### 13.2 Loading State
**Purpose**
- Keep users informed while data is being fetched

**Examples**
- Search results loading
- Destination details loading
- Planner generating results

**Behavior**
- Skeleton loading in card or section shape
- Smooth transitions

---

### 13.3 Error State
**Purpose**
- Communicate failures clearly and help the user recover

**Examples**
- Failed API request
- Invalid input
- Temporary outage

**Content**
- Clear error message
- Retry or try-again option
- Friendly guidance

---

## 14. Page-Level Component Composition

### 14.1 Landing Page
**Sections**
- Header
- Hero section
- Search bar
- Featured destination cards
- Trust or social proof block
- Footer

### 14.2 Destination Search Page
**Sections**
- Header
- Search bar
- Filter chip bar
- Results grid/list
- Empty/loading/error states
- Footer

### 14.3 Destination Details Page
**Sections**
- Header
- Destination hero
- Summary card
- Weather widget
- Attractions section
- Restaurants section
- Hotels section
- Map container
- Footer

### 14.4 Trip Planner Page
**Sections**
- Header
- Planner form
- Planner summary panel
- Recommendations section
- Footer

### 14.5 About Page
**Sections**
- Header
- Editorial content block
- Brand story / values
- Footer

### 14.6 Contact Page
**Sections**
- Header
- Contact form
- Contact information block
- Footer

---

## 15. Interaction and Motion Guidance

### 15.1 Hover States
- Subtle card lift or shadow change
- Button color shift
- Soft transition timing

### 15.2 Focus States
- Clear, accessible focus outline
- Consistent across interactive elements

### 15.3 Motion Style
- Light and calm
- Short transitions
- No heavy animation
- Supports clarity rather than decoration

---

## 16. Accessibility Requirements

Every component should support:
- Sufficient color contrast
- Keyboard navigation
- Visible focus states
- Semantic HTML structure
- Readable text sizes and spacing
- Touch-friendly targets
- Clear labeled forms and actions

---

## 17. Responsive Behavior Summary

### Mobile
- Single-column flows
- Large tap targets
- Compact but airy cards
- Sticky bottom actions where useful

### Tablet
- Balanced two-column layout where appropriate
- Card grids remain readable and spacious

### Desktop
- Wider content containers
- More generous whitespace
- Stronger hero presence and more visible hierarchy

---

## 18. Implementation Notes for Frontend Architecture

### Component Reusability Strategy
- Use shared primitives for buttons, inputs, cards, and layout containers
- Compose larger sections from smaller reusable blocks
- Keep page-specific logic isolated from shared UI components

### State Handling Strategy
- Local UI state for forms and interactions
- Shared state only where needed across page-level sections
- Clear handling for loading, empty, and error states

### Content Modeling Guidance
- Components should be flexible enough to support destination, itinerary, and travel content without over-customization
- Prefer generic reusable components with clear variant options

---

## 19. Component Priority for MVP

### High Priority
- Header — **Implemented** (Navbar.jsx)
- Hero section — **Implemented** (HeroSection.jsx in sections/)
- Search bar — **Implemented** (SearchBar.jsx)
- Destination card — **Implemented** (DestinationCard.jsx)
- Trip planner form — **Implemented** (DestinationSelector, DatePicker, BudgetSelector, TravelersSelector, ThemeSelector)
- Summary card — **Implemented** (TripSummary.jsx)
- Footer — **Implemented** (Footer.jsx)
- Loading and empty states — **Implemented** (LoadingState.jsx, EmptyState.jsx, ErrorState.jsx)
- Form elements — **Implemented** (Input.jsx, ContactForm.jsx)

### Medium Priority
- Filters and chips — **Implemented** (FilterBar.jsx)
- Weather widget — **Implemented** (WeatherWidget.jsx)
- Map container — **Implemented** (MapPlaceholder.jsx)
- Contact form enhancements — **Implemented** (ContactForm.jsx with validation)
- Modal and drawer patterns — Deferred

### Lower Priority
- Advanced animations — Deferred
- Highly customized interactive widgets — Deferred
- Complex dashboard-style components — Deferred

---

## 20. Shared Components Implemented (Frontend Review)

The following shared components were created during the frontend review and refactoring phase:

- **StarRating.jsx** — 5-star display with filled/half/empty states using design tokens
- **PriceLevel.jsx** — price level indicator with token-based colors
- **SectionHeader.jsx** — reusable eyebrow + heading + description pattern
- **DetailCard.jsx** — flexible card for attractions, restaurants, and hotels with image, badge, rating, price level

> **Note:** `LazyImage.jsx`, `poolUtils.js`, and `attractionsData.js` were removed during the production readiness review as dead code (no longer imported after API integration). Image lazy loading is now handled via native `loading="lazy"` attribute on `<img>` tags.

---

## 20. Final Component Library Direction

The Travel Planner frontend should be built around a calm, premium, and reusable component system that balances:
- Visual elegance
- Strong content hierarchy
- Responsive usability
- Clear planning functionality
- A lightweight and maintainable architecture

This library should serve as the foundation for implementing the landing page, destination exploration experience, destination detail pages, planner flow, about page, and contact experience in a consistent and scalable way.
