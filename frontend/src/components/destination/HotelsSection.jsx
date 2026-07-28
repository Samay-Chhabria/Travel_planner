import { useCallback } from 'react';
import PageContainer from '../layout/PageContainer';
import SectionHeader from '../common/SectionHeader';
import DetailCard from '../common/DetailCard';
import useFetch from '../../hooks/useFetch';
import { getHotelsForDestination } from '../../services/hotelsService';
import { formatPriceLevel } from '../../utils/constants';

const FALLBACK_IMAGE =
  'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=400&q=80';

function HotelsSkeleton() {
  return (
    <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4" aria-label="Loading hotels" role="status">
      {Array.from({ length: 4 }).map((_, i) => (
        <div
          key={i}
          className="animate-pulse overflow-hidden rounded-card border border-border bg-surface shadow-card"
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
      <span className="sr-only">Loading hotels...</span>
    </div>
  );
}

export default function HotelsSection({ destinationId, destinationName }) {
  const fetchHotels = useCallback(
    () => getHotelsForDestination(destinationId, { limit: 6 }),
    [destinationId],
  );

  const { data: hotels, loading, error, execute: retry } = useFetch(
    fetchHotels,
    [destinationId],
  );

  return (
    <section className="bg-surface py-12 md:py-16" aria-labelledby="hotels-heading">
      <PageContainer>
        <SectionHeader
          eyebrow="Where to stay"
          title={`Recommended hotels in ${destinationName || 'this destination'}`}
          description="Find the perfect accommodation for your stay, from luxury to budget-friendly options."
          id="hotels"
        />

        <div className="mt-8">
          {loading && <HotelsSkeleton />}

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
                Hotels unavailable
              </h3>
              <p className="mb-6 max-w-sm text-secondary">
                {error || 'Unable to load hotel information for this destination.'}
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

          {!loading && !error && hotels && hotels.length === 0 && (
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
                    d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"
                  />
                </svg>
              </div>
              <h3 className="mb-2 text-lg font-semibold text-primary">
                No hotels found
              </h3>
              <p className="max-w-sm text-secondary">
                Hotel recommendations are not available for this destination yet.
              </p>
            </div>
          )}

          {!loading && !error && hotels && hotels.length > 0 && (
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {hotels.map((hotel) => {
                const price = formatPriceLevel(hotel.price_level);
                return (
                  <DetailCard
                    key={hotel.id}
                    image={hotel.image_url || FALLBACK_IMAGE}
                    imageAlt={hotel.name}
                    badge={price.label}
                    title={hotel.name}
                    description={hotel.description}
                    rating={hotel.rating}
                    priceLevel={price.display}
                    variant="surface"
                  />
                );
              })}
            </div>
          )}
        </div>
      </PageContainer>
    </section>
  );
}
