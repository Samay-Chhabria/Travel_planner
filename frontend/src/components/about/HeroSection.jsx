import PageContainer from '../layout/PageContainer';

export default function HeroSection() {
  return (
    <div className="relative overflow-hidden bg-background pt-16 pb-12 md:pt-24 md:pb-16">
      <PageContainer>
        <div className="max-w-3xl">
          <p className="mb-4 text-sm font-semibold uppercase tracking-widest text-accent">
            About Us
          </p>
          <h1 className="text-4xl font-bold leading-tight text-primary sm:text-5xl lg:text-6xl">
            Travel made{' '}
            <span className="text-accent">simple</span>,{' '}
            <span className="text-highlight">beautiful</span>, and{' '}
            <span className="text-accent">personal</span>
          </h1>
          <p className="mt-6 max-w-2xl text-lg leading-relaxed text-secondary">
            Travel Planner is a modern platform that helps you discover amazing
            destinations and create personalized trip itineraries — all in one place.
            Built with care for travelers who love exploring the world.
          </p>
        </div>
      </PageContainer>

      <div
        className="absolute -right-20 -top-20 h-64 w-64 rounded-full bg-accent/5 blur-3xl"
        aria-hidden="true"
      />
      <div
        className="absolute -bottom-16 -left-16 h-48 w-48 rounded-full bg-highlight/5 blur-3xl"
        aria-hidden="true"
      />
    </div>
  );
}
