import { useCallback } from 'react';
import PageContainer from '../layout/PageContainer';
import SectionHeader from '../common/SectionHeader';
import DetailCard from '../common/DetailCard';
import useFetch from '../../hooks/useFetch';
import { getAttractionsForDestination } from '../../services/attractionsService';

const FALLBACK_IMAGE =
  'https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=400&q=80';

function AttractionsSkeleton() {
  return (
    <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4" aria-label="Loading attractions" role="status">
      {Array.from({ length: 4 }).map((_, i) => (
        <div
          key={i}
          className="animate-pulse overflow-hidden rounded-card border border-border bg-background shadow-card"
        >
          <div className="aspect-[4/3] bg-border/60" />
          <div className="space-y-3 p-4">
            <div className="flex items-start justify-between gap-2">
              <div className="h-5 w-2/3 rounded bg-border/60" />
              <div className="h-5 w-10 rounded bg-border/40" />
            </div>
            <div className="h-4 w-full rounded bg-border/40" />
            <div className="h-4 w-5/6 rounded bg-border/40" />
            <div className="mt-3 h-4 w-16 rounded bg-border/40" />
          </div>
        </div>
      ))}
      <span className="sr-only">Loading attractions...</span>
    </div>
  );
}

export default function AttractionsSection({ destinationId, destinationName }) {
  const fetchAttractions = useCallback(
    () => getAttractionsForDestination(destinationId, { limit: 6 }),
    [destinationId],
  );

  const { data: attractions, loading, error, execute: retry } = useFetch(
    fetchAttractions,
    [destinationId],
  );

  return (
    <section className="bg-surface py-12 md:py-16" aria-labelledby="attractions-heading">
      <PageContainer>
        <SectionHeader
          eyebrow="Things to do"
          title={`Popular attractions in ${destinationName || 'this destination'}`}
          description="Discover the best experiences and landmarks this destination has to offer."
          id="attractions"
        />

        <div className="mt-8">
          {loading && <AttractionsSkeleton />}

          {!loading && error && (
            <div className="flex flex-col items-center justify-center py-12 text-center">
              <div className="mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-highlight/10">
                <svg
                  className="h-8 w-8 text-highlight"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                  aria-hidden="true"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={1.5}
                    d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
                  />
                </svg>
              </div>
              <h3 className="mb-2 text-lg font-semibold text-primary">
                Attractions unavailable
              </h3>
              <p className="mb-6 max-w-sm text-secondary">
                {error || 'Unable to load attraction information for this destination.'}
              </p>
              <button
                type="button"
                onClick={() => retry()}
                className="inline-flex min-h-[44px] items-center justify-center gap-2 rounded-pill bg-accent px-6 py-3 font-medium text-white shadow-sm transition-all duration-200 hover:bg-accent/90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2"
              >
                Try Again
              </button>
            </div>
          )}

          {!loading && !error && attractions && attractions.length === 0 && (
            <div className="flex flex-col items-center justify-center py-12 text-center">
              <div className="mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-background">
                <svg
                  className="h-8 w-8 text-secondary/60"
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
              <h3 className="mb-2 text-lg font-semibold text-primary">
                No attractions found
              </h3>
              <p className="max-w-sm text-secondary">
                Attraction recommendations are not available for this destination yet.
              </p>
            </div>
          )}

          {!loading && !error && attractions && attractions.length > 0 && (
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {attractions.map((attraction) => (
                <DetailCard
                  key={attraction.id}
                  image={attraction.image_url || FALLBACK_IMAGE}
                  imageAlt={attraction.name}
                  badge={attraction.category}
                  title={attraction.name}
                  description={attraction.description}
                  rating={attraction.rating}
                  variant="background"
                />
              ))}
            </div>
          )}
        </div>
      </PageContainer>
    </section>
  );
}
