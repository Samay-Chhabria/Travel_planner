import { useParams, Link } from 'react-router-dom';
import { useCallback } from 'react';
import DestinationHero from '../components/destination/DestinationHero';
import OverviewSection from '../components/destination/OverviewSection';
import WeatherWidget from '../components/destination/WeatherWidget';
import AttractionsSection from '../components/destination/AttractionsSection';
import HotelsSection from '../components/destination/HotelsSection';
import RestaurantsSection from '../components/destination/RestaurantsSection';
import MapPlaceholder from '../components/destination/MapPlaceholder';
import PlanTripCTA from '../components/destination/PlanTripCTA';
import PageContainer from '../components/layout/PageContainer';
import useFetch from '../hooks/useFetch';
import { getDestinationById } from '../services/destinationService';

function DestinationSkeleton() {
  return (
    <div className="bg-background animate-pulse" role="status" aria-label="Loading destination">
      <div className="h-64 bg-border/40 md:h-96" />
      <PageContainer className="py-12">
        <div className="space-y-4">
          <div className="h-8 w-64 rounded bg-border/40" />
          <div className="h-4 w-96 rounded bg-border/30" />
          <div className="h-4 w-80 rounded bg-border/30" />
        </div>
      </PageContainer>
      <span className="sr-only">Loading destination details...</span>
    </div>
  );
}

export default function DestinationDetailsPage() {
  const { slug } = useParams();

  const fetchDestination = useCallback(
    () => getDestinationById(slug),
    [slug],
  );

  const { data: destination, loading, error } = useFetch(
    fetchDestination,
    [slug],
  );

  if (loading) {
    return <DestinationSkeleton />;
  }

  if (error || !destination) {
    return (
      <div className="bg-background">
        <PageContainer className="flex flex-col items-center justify-center py-24 text-center">
          <div className="mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-highlight/10">
            <svg
              className="h-10 w-10 text-highlight"
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
          <h1 className="mb-2 text-2xl font-bold text-primary">Destination not found</h1>
          <p className="mb-8 max-w-md text-secondary">
            {error || 'The destination you\'re looking for doesn\'t exist or may have been removed.'}
          </p>
          <Link
            to="/explore"
            className="inline-flex min-h-[44px] items-center justify-center gap-2 rounded-pill bg-accent px-6 py-3 font-medium text-white shadow-sm transition-all duration-200 hover:bg-accent/90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2"
          >
            Browse Destinations
          </Link>
        </PageContainer>
      </div>
    );
  }

  return (
    <div className="bg-background">
      <DestinationHero destination={destination} />
      <OverviewSection destination={destination} />
      <WeatherWidget destinationId={destination.id} />
      <AttractionsSection destinationId={destination.id} destinationName={destination.name} />
      <RestaurantsSection destinationId={destination.id} destinationName={destination.name} />
      <HotelsSection destinationId={destination.id} destinationName={destination.name} />
      <MapPlaceholder destination={destination} />
      <PlanTripCTA destination={destination} />
    </div>
  );
}
