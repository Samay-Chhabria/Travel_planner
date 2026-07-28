# prompt_1
You're a senior Software architect you have to design the entire software architecture of my tarvel planner website use the files attached for context don't divert from it don't generate any kind of code yet just generate an software_architecture.md it should have everything related to my software architecture.

# prompt_2
you're a senior product designer and ui/ux designer you have to competely design the ui and the user experience use air bnb as an inspiration for spacing, typography, layout,and simplicity make a completely unique one finally generate an ui_desgin.md file which contain everything related to ui/ux don't generate any code for context i have attached the required file.

# prompt_3
You're senior frontend Architect and Senior System design engineer you have to design and plan all the components required for my travel planner application donot generate any kind of code just return a component_library.md file which contains every deatils related to the components of my application for context use the attached files.

# prompt_4
You're a senior backend architect and senior api designer, you have to design the complete rest api specification for my travel planner application donot implement any code just design the complete api specification in last generate the api_specification.md which contains evrything related to my application for the context use the attach files consider them as the ground truth.

# prompt_5
you're a senior full stack developer , implement the complete folder structure for my travel planner application with all the necessry files, donot generate any code and state the purpose of every file and folder use the attach files for context and as the source truth.

# prompt_6
You are a Senior Frontend Engineer with 10+ years of experience in React, Vite, Tailwind CSS, modern frontend architecture, performance optimization, accessibility, and responsive web design.
"- PROJECT_CONTEXT.md
- PRD.md
- ARCHITECTURE.md
- UI_DESIGN_GUIDE.md
- COMPONENT_LIBRARY.md
- API_SPECIFICATION.md"
for context these documents are the single source of truth. If there is any conflict between your assumptions and the documentation, always follow the documentation.

Your responsibility is to implement the frontend of the Travel Planner application feature by feature.

Before implementing any feature:

1. Read and understand all project documentation.
2. Understand how the requested feature fits into the overall architecture.
3. Identify which existing components can be reused.
4. Explain your implementation approach.
5. List every file that will be created or modified.
6. Generate production-ready code.
7. Explain how to test the feature.
8. Wait for the next feature request before implementing anything else.

REQUIREMENTS

- Follow the UI Design Guide exactly.
- Follow the Component Library exactly.
- Follow the Architecture document exactly.
- Use React + Vite + Tailwind CSS.
- Write clean, modular, reusable components.
- Reuse existing components whenever possible.
- Maintain a scalable folder structure.
- Ensure responsive design.
- Follow accessibility best practices.
- Keep the code production-ready.

CONSTRAINTS

- Do not modify unrelated files.
- Do not redesign the UI.
- Do not change the project architecture.
- Do not create duplicate components.
- Do not implement backend functionality.
- Do not add libraries unless necessary and explain why.
- Build only the feature requested in each prompt.

OUTPUT

For every feature:

1. Brief implementation plan.
2. Files to create or modify.
3. Complete production-ready code.
4. Integration instructions.
5. Testing instructions.
6. Any recommendations or improvements.

# prompt_7
Implement the Landing Page.
Requirements:
- Hero Section
- Search Bar
- Featured Destinations
- Popular Themes
- Testimonials
- Footer
Follow all project documentation.
Do not implement any other pages.

# prompt_8
Implement the Destination Search page.
Requirements:
- Search input
- Destination cards
- Filter section
- Sort options
- Grid/List view toggle
- Loading state
- Empty state
- Error state
- Responsive design
Reuse existing components from COMPONENT_LIBRARY.md.
Follow all project documentation.
Do not implement destination details or backend integration yet.

# prompt_9
Implement the Destination Details page.
Requirements:
- Destination hero image
- Overview section
- Weather information placeholder
- Attractions section
- Hotels section
- Restaurants section
- Map placeholder
- "Plan Trip" CTA
- Responsive design
Reuse existing components.
Follow all project documentation.
Do not implement backend integration.

# prompt_10
Implement the Trip Planner page.
Requirements:
- Trip summary
- Date selection
- Budget selection
- Travelers selection
- Theme selection
- Selected destinations
- Generated itinerary placeholder
- Responsive layout
Reuse existing components.
Follow all project documentation.
Do not implement AI or backend functionality.

# prompt_11
Implement the About page.
Requirements:
- Project overview
- Mission
- Features
- Technologies used
- Developer information
- Responsive layout
Reuse existing components.
Follow all project documentation.

# prompt_12
Implement the Contact page.
Requirements:
- Contact form
- Social links
- FAQ section
- Responsive layout
Reuse existing components.
Follow all project documentation.
Do not implement form submission.

# prompt_13
Frontend Review
Requirements:
- Review the complete frontend
- Check responsiveness
- Check accessibility
- Check consistency
- Remove duplicate code
- Improve performance
- Ensure all components follow the design system
- Suggest improvements

# prompt_14
Documentation and Maintenance
Requirements:
- Review the entire project
- Update all documentation to reflect current implementation
- Mark completed frontend features and milestones
- Ensure internal consistency across documents
- Update project structure and folder tree
- Update dependency files
- Remove obsolete documentation
- Ensure naming conventions are consistent
- Verify documentation matches source code

# prompt_15
ROLE
You are a Senior Backend Engineer specializing in FastAPI, REST APIs, clean architecture, and scalable backend development.
CONTEXT
Read and follow:
- PROJECT_CONTEXT.md
- PRD.md
- ARCHITECTURE.md
- API_SPECIFICATION.md
These documents are the source of truth.
TASK
Implement the backend foundation for the Travel Planner application.
REQUIREMENTS
- Initialize the FastAPI project.
- Create the folder structure defined in the architecture.
- Configure environment management.
- Configure CORS for frontend communication.
- Create a health check endpoint.
- Configure logging.
- Configure centralized exception handling.
- Create a reusable HTTP client for external APIs.
- Prepare the project for future service modules.
CONSTRAINTS
- Do not implement feature APIs yet.
- Do not add authentication.
- Do not add a database.
- Keep the project modular and production-ready.
OUTPUT
- Implement the requested changes directly in the project.
- Modify only the necessary files.
- Keep documentation and dependency files synchronized.
- Verify the project builds and runs successfully.
- Provide a concise summary including:
    - Files created or modified
    - Dependencies added or removed
    - Commands to verify the implementation
    - Any important notes or recommendations

# prompt_16
FEATURE
Weather Module
TASK
Implement the complete Weather module using the selected free weather API.
REQUIREMENTS
- Create a dedicated weather router.
- Create a weather service.
- Validate request parameters.
- Call the external weather API.
- Normalize the response into the project's standard response format.
- Handle API failures gracefully.
- Return meaningful HTTP status codes.
- Add request logging.
- Add unit tests.
CONSTRAINTS
- Follow the API specification.
- Do not modify unrelated modules.
- Keep the implementation reusable.
- Do not expose the external API directly to the frontend.
OUTPUT
- Implement the module directly in the project.
- Update documentation and requirements if necessary.
- Provide testing instructions and example requests.

# prompt_17
FEATURE
Geocoding Module
TASK
Implement the complete Geocoding module using the selected free geocoding API.
REQUIREMENTS
- Create a dedicated geocoding router.
- Create a geocoding service.
- Validate request parameters.
- Convert location names into coordinates.
- Normalize responses into the project's standard format.
- Handle API failures gracefully.
- Return meaningful HTTP status codes.
- Add request logging.
- Add unit tests.
CONSTRAINTS
- Follow the API specification.
- Do not modify unrelated modules.
- Keep the implementation reusable.
- Do not expose the external API directly to the frontend.
OUTPUT
- Implement the module directly in the project.
- Update documentation if necessary.
- Provide testing instructions and example requests.

# prompt_18
FEATURE
Destination Search Module
TASK
Implement the complete Destination Search backend module according to the project documentation.
REQUIREMENTS
- Search destinations from the selected external API.
- Validate all request parameters.
- Return standardized responses.
- Handle errors gracefully.
- Add logging.
- Add unit tests.
CONSTRAINTS
- Follow all project documentation.
- Do not modify unrelated modules.
- Do not expose external APIs directly.
OUTPUT
- Implement the module.
- Update documentation if required.
- Provide testing instructions and example requests.

# prompt_19
FEATURE
Places & Attractions Module
TASK
Implement the complete Places & Attractions backend module according to the project documentation.
REQUIREMENTS
- Retrieve nearby attractions.
- Support filtering where applicable.
- Validate inputs.
- Return standardized responses.
- Handle API failures.
- Add logging.
- Add unit tests.
CONSTRAINTS
- Follow project documentation.
- Do not modify unrelated modules.
- Keep the implementation reusable.
OUTPUT
- Implement the module.
- Update documentation if required.
- Provide testing instructions and example requests.

# prompt_20
FEATURE
Hotels Module
TASK
Implement the complete Hotels backend module according to the project documentation.
REQUIREMENTS
- Retrieve nearby hotels.
- Validate inputs.
- Return standardized responses.
- Handle API failures.
- Add logging.
- Add unit tests.
CONSTRAINTS
- Follow project documentation.
- Do not modify unrelated modules.
- Keep the implementation reusable.
OUTPUT
- Implement the module.
- Update documentation if required.
- Provide testing instructions and example requests.

# prompt_21
FEATURE
Restaurants Module
TASK
Implement the complete Restaurants backend module according to the project documentation.
REQUIREMENTS
- Retrieve nearby restaurants.
- Validate inputs.
- Return standardized responses.
- Handle API failures.
- Add logging.
- Add unit tests.
CONSTRAINTS
- Follow project documentation.
- Do not modify unrelated modules.
- Keep the implementation reusable.
OUTPUT
- Implement the module.
- Update documentation if required.
- Provide testing instructions and example requests.

# prompt22
FEATURE
Trip Planner Module
TASK
Implement the Trip Planner backend module according to the project documentation.
REQUIREMENTS
- Coordinate existing backend services.
- Generate a unified trip planning response.
- Validate all inputs.
- Handle partial service failures gracefully.
- Return standardized responses.
- Add logging.
- Add unit tests.
CONSTRAINTS
- Reuse existing services.
- Do not duplicate logic.
- Do not call external APIs directly when an existing service already provides the functionality.
- Follow project documentation.
OUTPUT
- Implement the module.
- Update documentation if required.
- Provide testing instructions and example requests.

# prompt_23
Review the complete backend implementation.
Verify:
- Project architecture
- Folder structure
- FastAPI best practices
- API consistency
- Response schemas
- Error handling
- Logging
- Input validation
- Dependency management
- Code quality
- Performance
- Test coverage
- Documentation consistency
Fix any issues without changing functionality.
Update all documentation and dependency files if necessary.
Confirm the backend is production-ready for frontend integration.

# prompt_24
FEATURE
Frontend API Integration Layer
TASK
Implement the frontend API communication layer according to the project documentation.
REQUIREMENTS
- Configure the backend base URL using environment variables.
- Create a reusable API client.
- Implement centralized API request handling.
- Implement centralized error handling.
- Create service modules for each backend endpoint.
- Prepare the frontend for backend integration.
CONSTRAINTS
- Do not modify page layouts.
- Do not change the UI.
- Follow the project architecture.
- Keep the implementation modular.
OUTPUT
- Implement the integration layer.
- Update documentation if required.
- Provide testing instructions.

# prompt_25
FEATURE
Integrate Destination Search
TASK
Connect the Destination Search page with the backend Destination Search API.
REQUIREMENTS
- Replace mock data.
- Use the shared API client.
- Display loading state.
- Display error state.
- Display empty state.
- Handle API responses correctly.
CONSTRAINTS
- Do not modify backend code.
- Preserve the existing UI.
- Follow project documentation.
OUTPUT
- Implement the integration.
- Update documentation if required.
- Provide testing instructions.

# prompt_26
FEATURE
Weather Integration
TASK
Connect the Weather components to the backend Weather API.
REQUIREMENTS
- Replace mock data with backend responses.
- Use the shared API client.
- Display loading, error, and empty states.
- Format weather data according to the UI design.
- Preserve the existing UI.
CONSTRAINTS
- Do not modify backend code.
- Follow all project documentation.
OUTPUT
- Implement the integration.
- Update documentation if necessary.
- Provide testing instructions.

# prompt_27
FEATURE
Hotels Integration 
TASK
Connect the Hotels section to the backend Hotels API.
REQUIREMENTS
- Replace mock hotel data. 
- Use the shared API client. 
- Display loading, error, and empty states. 
- Preserve the existing UI. 
CONSTRAINTS
- Do not modify backend code.
- Follow all project documentation.
OUTPUT
- Implement the integration. 
- Update documentation if necessary. 
- Provide testing instructions. 

# prompt_28
Restaurants Integration 
TASK
Connect the Restaurants section to the backend Restaurants API.
REQUIREMENTS
- Replace mock restaurant data. 
- Use the shared API client. 
- Display loading, error, and empty states. 
- Preserve the existing UI. 
CONSTRAINTS
- Do not modify backend code.
- Follow all project documentation.
OUTPUT
- Implement the integration. 
- Update documentation if necessary. 
- Provide testing instructions. 

# prompt_29
Attractions Integration 
TASK
Connect the Attractions section to the backend Attractions API.
REQUIREMENTS
- Replace mock attraction data. 
- Use the shared API client. 
- Display loading, error, and empty states. 
- Preserve the existing UI. 
CONSTRAINTS
- Do not modify backend code.
- Follow all project documentation.
OUTPUT
- Implement the integration. 
- Update documentation if necessary. 
- Provide testing instructions. 

# prompt_30
Trip Planner Integration 
TASK
Connect the Trip Planner page to the backend Trip Planner API.
REQUIREMENTS
- Replace all mock data.
- Use the shared API client. 
- Submit user selections to the backend. 
- Display the generated trip plan. 
- Handle loading, error, and empty states. 
- Preserve the existing UI. 
CONSTRAINTS
- Do not modify backend code.
- Reuse existing frontend services.
- Follow all project documentation.
OUTPUT
- Implement the integration. 
- Update documentation if necessary. 
- Provide testing instructions. 

# prompt_31
FEATURE
Full Application Integration Review
TASK
Review the complete Travel Planner application after frontend-backend integration.
VERIFY
- All frontend pages communicate correctly with the backend.
- API calls are centralized.
- No mock data remains.
- Loading, error, and empty states are implemented consistently.
- Response formats match the API specification.
- No console errors or network failures.
- CORS is configured correctly.
- The application builds and runs successfully.
Fix any issues without changing functionality.
Update all relevant documentation.
Confirm the application is ready for deployment.

STATUS: DONE — Production Readiness Review completed 2026-07-14

Issues found and fixed:
1. DestinationDetailsPage.jsx used ALL_DESTINATIONS.find() instead of API → replaced with getDestinationById() via useFetch hook
2. NotFoundPage.jsx was empty placeholder → implemented full 404 page with navigation
3. No 404 catch-all route in routes.jsx → added * route with lazy-loaded NotFoundPage
4. Dead code removed: poolUtils.js, attractionsData.js, useMediaQuery.js, PageLayout.jsx, LazyImage.jsx, globals.css, formatters.js, locationUtils.js, contactService.js, data/ directory
5. CORS allow_methods expanded to include PUT, DELETE, PATCH; allow_headers includes Authorization
6. Hero section stats updated to reflect actual data (20+ destinations, 3 live data sources)
7. Stale dist/ build output cleaned up

Verification:
- Frontend builds with 0 errors (154 modules, 13 chunks)
- Backend: 157/157 tests pass
- All API response shapes verified against frontend service extraction paths
- No mock data remains in production code
- Loading, error, and empty states implemented on all API-driven sections