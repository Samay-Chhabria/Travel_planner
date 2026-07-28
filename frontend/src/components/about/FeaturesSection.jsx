import SectionWrapper from '../layout/SectionWrapper';

const FEATURES = [
  {
    title: 'Destination Discovery',
    description: 'Browse and search through a curated collection of travel destinations worldwide with detailed information.',
    icon: (
      <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
      </svg>
    ),
  },
  {
    title: 'Trip Planning',
    description: 'Create personalized itineraries based on your budget, travel dates, group size, and preferred theme.',
    icon: (
      <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
      </svg>
    ),
  },
  {
    title: 'Weather Insights',
    description: 'Get real-time weather data for your destinations to plan the perfect time for your trip.',
    icon: (
      <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
      </svg>
    ),
  },
  {
    title: 'Local Experiences',
    description: 'Discover top attractions, restaurants, and hotels at each destination for an authentic experience.',
    icon: (
      <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
      </svg>
    ),
  },
  {
    title: 'Responsive Design',
    description: 'Enjoy a seamless experience across all devices — desktop, tablet, and mobile.',
    icon: (
      <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
      </svg>
    ),
  },
  {
    title: 'Airbnb-Inspired',
    description: 'Clean, modern interface with warm aesthetics, generous spacing, and intuitive navigation.',
    icon: (
      <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
      </svg>
    ),
  },
];

export default function FeaturesSection() {
  return (
    <SectionWrapper id="features" background="default" ariaLabelledby="features-heading">
      <div className="text-center mb-12">
        <h2
          id="features-heading"
          className="text-3xl font-bold text-primary sm:text-4xl"
        >
          Platform Features
        </h2>
        <p className="mt-4 max-w-2xl mx-auto text-secondary">
          Everything you need to plan your next adventure
        </p>
      </div>

      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {FEATURES.map((feature) => (
          <div
            key={feature.title}
            className="group rounded-card border border-border bg-surface p-6 transition-all duration-200 hover:border-accent/20 hover:shadow-elevated"
          >
            <div className="mb-4 inline-flex h-12 w-12 items-center justify-center rounded-xl bg-highlight/10 text-highlight transition-colors duration-200 group-hover:bg-highlight/20">
              {feature.icon}
            </div>
            <h3 className="mb-2 text-lg font-semibold text-primary">
              {feature.title}
            </h3>
            <p className="text-sm leading-relaxed text-secondary">
              {feature.description}
            </p>
          </div>
        ))}
      </div>
    </SectionWrapper>
  );
}
