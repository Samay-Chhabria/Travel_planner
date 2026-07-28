import { useEffect, useState } from 'react';
import SectionWrapper from '../layout/SectionWrapper';
import DestinationCard from '../cards/DestinationCard';
import { DestinationGridSkeleton } from '../feedback/LoadingState';
import Button from '../common/Button';
import { getFeaturedDestinations } from '../../services/destinationService';
import { FALLBACK_FEATURED_DESTINATIONS } from '../../utils/constants';

export default function FeaturedDestinations() {
  const [destinations, setDestinations] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let isMounted = true;

    async function fetchFeatured() {
      try {
        const data = await getFeaturedDestinations(6);
        if (isMounted) {
          setDestinations(
            data.length > 0 ? data : FALLBACK_FEATURED_DESTINATIONS
          );
        }
      } catch {
        if (isMounted) {
          setDestinations(FALLBACK_FEATURED_DESTINATIONS);
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    fetchFeatured();

    return () => {
      isMounted = false;
    };
  }, []);

  return (
    <SectionWrapper background="default" ariaLabelledby="featured-heading">
      <div className="mb-10 flex flex-col items-start justify-between gap-4 md:mb-12 md:flex-row md:items-end">
        <div className="max-w-2xl">
          <p className="mb-2 text-sm font-medium uppercase tracking-widest text-accent">
            Curated picks
          </p>
          <h2
            id="featured-heading"
            className="text-3xl font-bold text-primary md:text-4xl"
          >
            Featured destinations
          </h2>
          <p className="mt-3 text-secondary md:text-lg">
            Handpicked places to inspire your next journey — from iconic cities
            to serene escapes.
          </p>
        </div>
        <Button variant="secondary" to="/explore">
          View all destinations
        </Button>
      </div>

      {loading ? (
        <DestinationGridSkeleton count={6} />
      ) : (
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {destinations.map((destination) => (
            <DestinationCard key={destination.id} destination={destination} />
          ))}
        </div>
      )}
    </SectionWrapper>
  );
}
