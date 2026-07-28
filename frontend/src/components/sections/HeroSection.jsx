import SearchBar from '../search/SearchBar';
import Button from '../common/Button';
import PageContainer from '../layout/PageContainer';

const HERO_IMAGE =
  'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=1920&q=80';

export default function HeroSection() {
  return (
    <section
      className="relative overflow-hidden bg-primary"
      aria-labelledby="hero-heading"
    >
      <div className="absolute inset-0" aria-hidden="true">
        <img
          src={HERO_IMAGE}
          alt=""
          className="h-full w-full object-cover opacity-60"
        />
        <div className="absolute inset-0 bg-gradient-to-r from-primary/90 via-primary/70 to-primary/40" />
      </div>

      <PageContainer className="relative py-20 md:py-28 lg:py-32">
        <div className="mx-auto max-w-3xl text-center lg:max-w-4xl">
          <p className="mb-4 text-sm font-medium uppercase tracking-widest text-highlight md:text-base">
            Plan smarter. Travel better.
          </p>
          <h1
            id="hero-heading"
            className="text-balance text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl"
          >
            Discover your next adventure with confidence
          </h1>
          <p className="mx-auto mt-6 max-w-2xl text-base leading-relaxed text-white/85 md:text-lg">
            Explore curated destinations, browse inspiring travel themes, and
            start planning trips that feel calm, clear, and unforgettable.
          </p>

          <div className="mx-auto mt-10 max-w-2xl">
            <SearchBar />
          </div>

          <div className="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Button variant="highlight" size="lg" to="/explore">
              Explore Destinations
            </Button>
            <Button
              variant="secondary"
              size="lg"
              to="/planner"
              className="border-white/30 bg-white/10 text-white hover:bg-white/20"
            >
              Start Planning
            </Button>
          </div>

          <dl className="mt-12 grid grid-cols-3 gap-4 border-t border-white/20 pt-8 md:gap-8">
            <div>
              <dt className="sr-only">Destinations</dt>
              <dd className="text-2xl font-bold text-white md:text-3xl">20+</dd>
              <dd className="mt-1 text-xs text-white/70 md:text-sm">Destinations</dd>
            </div>
            <div>
              <dt className="sr-only">Travel themes</dt>
              <dd className="text-2xl font-bold text-white md:text-3xl">6</dd>
              <dd className="mt-1 text-xs text-white/70 md:text-sm">Travel Themes</dd>
            </div>
            <div>
              <dt className="sr-only">Data sources</dt>
              <dd className="text-2xl font-bold text-white md:text-3xl">3</dd>
              <dd className="mt-1 text-xs text-white/70 md:text-sm">Live Data Sources</dd>
            </div>
          </dl>
        </div>
      </PageContainer>
    </section>
  );
}
