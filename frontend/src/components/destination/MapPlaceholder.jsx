import PageContainer from '../layout/PageContainer';

export default function MapPlaceholder({ destination }) {
  const { name, country } = destination;

  return (
    <section className="bg-background py-12 md:py-16" aria-labelledby="map-heading">
      <PageContainer>
        <div className="mb-8">
          <p className="mb-2 text-sm font-medium uppercase tracking-widest text-accent">
            Location
          </p>
          <h2 id="map-heading" className="text-2xl font-bold text-primary md:text-3xl">
            Where to find {name}
          </h2>
        </div>

        <div className="overflow-hidden rounded-card border border-border bg-surface shadow-card">
          <div className="relative flex aspect-[16/9] items-center justify-center bg-gradient-to-br from-accent/5 to-highlight/5 md:aspect-[21/9]">
            <div className="absolute inset-0 opacity-10" aria-hidden="true">
              <svg className="h-full w-full" viewBox="0 0 800 400" fill="none">
                <path d="M0 200 Q200 100 400 200 Q600 300 800 200" stroke="currentColor" strokeWidth="2" />
                <path d="M0 250 Q200 150 400 250 Q600 350 800 250" stroke="currentColor" strokeWidth="1" />
                <circle cx="400" cy="200" r="8" fill="currentColor" />
                <circle cx="400" cy="200" r="16" stroke="currentColor" strokeWidth="2" fill="none" />
              </svg>
            </div>

            <div className="relative z-10 text-center">
              <div className="mb-4 inline-flex h-16 w-16 items-center justify-center rounded-full bg-accent/10">
                <svg
                  className="h-8 w-8 text-accent"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={1.5}
                    d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                  />
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={1.5}
                    d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                  />
                </svg>
              </div>
              <p className="text-lg font-semibold text-primary">{name}, {country}</p>
              <p className="mt-1 text-sm text-secondary">
                Interactive map coming soon with backend integration
              </p>
            </div>
          </div>
        </div>
      </PageContainer>
    </section>
  );
}
