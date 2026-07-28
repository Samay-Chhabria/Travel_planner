import Badge from '../common/Badge';
import PageContainer from '../layout/PageContainer';

export default function OverviewSection({ destination }) {
  const { highlights = [], best_time_to_visit: bestTime, description } = destination;

  return (
    <section className="bg-surface py-12 md:py-16" aria-labelledby="overview-heading">
      <PageContainer>
        <div className="grid gap-8 lg:grid-cols-3">
          <div className="lg:col-span-2">
            <p className="mb-2 text-sm font-medium uppercase tracking-widest text-accent">
              Overview
            </p>
            <h2 id="overview-heading" className="text-2xl font-bold text-primary md:text-3xl">
              About this destination
            </h2>
            <p className="mt-4 text-base leading-relaxed text-secondary md:text-lg">
              {description}
            </p>

            {highlights.length > 0 && (
              <div className="mt-6">
                <h3 className="mb-3 text-sm font-medium text-primary">Highlights</h3>
                <ul className="flex flex-wrap gap-2" aria-label="Destination highlights">
                  {highlights.map((highlight) => (
                    <li key={highlight}>
                      <Badge variant="accent">{highlight}</Badge>
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>

          <div className="rounded-card border border-border bg-background p-6">
            <h3 className="mb-4 text-sm font-semibold uppercase tracking-wide text-primary">
              Quick Info
            </h3>
            <dl className="space-y-4">
              {bestTime && (
                <div>
                  <dt className="text-sm text-secondary">Best time to visit</dt>
                  <dd className="mt-1 font-medium text-primary">{bestTime}</dd>
                </div>
              )}
              <div>
                <dt className="text-sm text-secondary">Region</dt>
                <dd className="mt-1 font-medium text-primary">{destination.region}</dd>
              </div>
              <div>
                <dt className="text-sm text-secondary">Country</dt>
                <dd className="mt-1 font-medium text-primary">{destination.country}</dd>
              </div>
              {destination.travel_type && (
                <div>
                  <dt className="text-sm text-secondary">Travel type</dt>
                  <dd className="mt-1 font-medium text-primary">{destination.travel_type}</dd>
                </div>
              )}
            </dl>
          </div>
        </div>
      </PageContainer>
    </section>
  );
}
