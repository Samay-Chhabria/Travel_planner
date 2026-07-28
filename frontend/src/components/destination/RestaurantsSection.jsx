import { useCallback } from 'react';
import PageContainer from '../layout/PageContainer';
import SectionHeader from '../common/SectionHeader';
import DetailCard from '../common/DetailCard';
import useFetch from '../../hooks/useFetch';
import { getRestaurantsForDestination } from '../../services/restaurantsService';
import { formatPriceLevel } from '../../utils/constants';

const FALLBACK_IMAGE =
  'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=400&q=80';

function RestaurantsSkeleton() {
  return (
    <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4" aria-label="Loading restaurants" role="status">
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
      <span className="sr-only">Loading restaurants...</span>
    </div>
  );
}

export default function RestaurantsSection({ destinationId, destinationName }) {
  const fetchRestaurants = useCallback(
    () => getRestaurantsForDestination(destinationId, { limit: 6 }),
    [destinationId],
  );

  const { data: restaurants, loading, error, execute: retry } = useFetch(
    fetchRestaurants,
    [destinationId],
  );

  return (
    <section className="bg-background py-12 md:py-16" aria-labelledby="restaurants-heading">
      <PageContainer>
        <SectionHeader
          eyebrow="Dining"
          title={`Where to eat in ${destinationName || 'this destination'}`}
          description="Savor local flavors and discover the best dining spots in the area."
          id="restaurants"
        />

        <div className="mt-8">
          {loading && <RestaurantsSkeleton />}

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
                Restaurants unavailable
              </h3>
              <p className="mb-6 max-w-sm text-secondary">
                {error || 'Unable to load restaurant information for this destination.'}
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

          {!loading && !error && restaurants && restaurants.length === 0 && (
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
                    d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              </div>
              <h3 className="mb-2 text-lg font-semibold text-primary">
                No restaurants found
              </h3>
              <p className="max-w-sm text-secondary">
                Restaurant recommendations are not available for this destination yet.
              </p>
            </div>
          )}

          {!loading && !error && restaurants && restaurants.length > 0 && (
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {restaurants.map((restaurant) => {
                const price = formatPriceLevel(restaurant.price_level);
                return (
                  <DetailCard
                    key={restaurant.id}
                    image={restaurant.image_url || FALLBACK_IMAGE}
                    imageAlt={restaurant.name}
                    badge={restaurant.cuisine_type}
                    title={restaurant.name}
                    description={restaurant.description}
                    rating={restaurant.rating}
                    priceLevel={price.display}
                    variant="background"
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
