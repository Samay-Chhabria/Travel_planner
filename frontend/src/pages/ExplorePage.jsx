import { useState, useEffect, useMemo } from 'react';
import { useSearchParams } from 'react-router-dom';
import PageContainer from '../components/layout/PageContainer';
import SearchBar from '../components/search/SearchBar';
import FilterBar from '../components/search/FilterBar';
import SortSelect from '../components/search/SortSelect';
import ViewToggle from '../components/search/ViewToggle';
import DestinationCard from '../components/cards/DestinationCard';
import { DestinationGridSkeleton } from '../components/feedback/LoadingState';
import EmptyState from '../components/feedback/EmptyState';
import ErrorState from '../components/feedback/ErrorState';
import useDebounce from '../hooks/useDebounce';
import {
  searchDestinations,
  getFeaturedDestinations,
} from '../services/destinationService';

export default function ExplorePage() {
  const [searchParams, setSearchParams] = useSearchParams();

  const initialQuery = searchParams.get('q') || '';
  const initialType = searchParams.get('type') || 'all';
  const initialRegion = searchParams.get('region') || 'all';

  const [query, setQuery] = useState(initialQuery);
  const [travelType, setTravelType] = useState(initialType);
  const [region, setRegion] = useState(initialRegion);
  const [sortBy, setSortBy] = useState('name-asc');
  const [view, setView] = useState('grid');
  const [destinations, setDestinations] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const debouncedQuery = useDebounce(query, 400);

  useEffect(() => {
    const params = new URLSearchParams();
    if (debouncedQuery) params.set('q', debouncedQuery);
    if (travelType !== 'all') params.set('type', travelType);
    if (region !== 'all') params.set('region', region);
    setSearchParams(params, { replace: true });
  }, [debouncedQuery, travelType, region, setSearchParams]);

  useEffect(() => {
    let isMounted = true;

    async function fetchDestinations() {
      setLoading(true);
      setError(null);

      try {
        let results;

        if (debouncedQuery && debouncedQuery.length >= 2) {
          results = await searchDestinations(debouncedQuery, { limit: 25 });
        } else {
          results = await getFeaturedDestinations(20);
        }

        if (isMounted) {
          setDestinations(results);
        }
      } catch (err) {
        if (isMounted) {
          setError(err.message || 'Failed to load destinations. Please try again.');
          setDestinations([]);
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    }

    fetchDestinations();

    return () => {
      isMounted = false;
    };
  }, [debouncedQuery]);

  const filteredAndSorted = useMemo(() => {
    let result = [...destinations];

    if (travelType !== 'all') {
      result = result.filter(
        (d) => d.travel_type?.toLowerCase() === travelType.toLowerCase()
      );
    }

    if (region !== 'all') {
      result = result.filter(
        (d) => d.region?.toLowerCase() === region.toLowerCase()
      );
    }

    result.sort((a, b) => {
      switch (sortBy) {
        case 'name-desc':
          return b.name.localeCompare(a.name);
        case 'region':
          return (a.region || '').localeCompare(b.region || '');
        case 'travel_type':
          return (a.travel_type || '').localeCompare(b.travel_type || '');
        case 'name-asc':
        default:
          return a.name.localeCompare(b.name);
      }
    });

    return result;
  }, [destinations, travelType, region, sortBy]);

  const handleClearFilters = () => {
    setQuery('');
    setTravelType('all');
    setRegion('all');
    setSortBy('name-asc');
  };

  const hasActiveFilters = query || travelType !== 'all' || region !== 'all';

  return (
    <div className="bg-background">
      <section className="border-b border-border bg-surface py-8 md:py-12">
        <PageContainer>
          <div className="mx-auto max-w-3xl text-center">
            <p className="mb-2 text-sm font-medium uppercase tracking-widest text-accent">
              Discover
            </p>
            <h1 className="text-3xl font-bold text-primary md:text-4xl">
              Explore destinations
            </h1>
            <p className="mt-3 text-secondary md:text-lg">
              Search, filter, and find your perfect travel destination from our curated collection.
            </p>
          </div>

          <div className="mx-auto mt-8 max-w-2xl">
            <SearchBar
              defaultValue={initialQuery}
              onSearch={setQuery}
              placeholder="Search destinations by name, country, or region..."
              size="lg"
              mode="controlled"
            />
          </div>
        </PageContainer>
      </section>

      <PageContainer className="py-8 md:py-12">
        <div className="mb-6 flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
          <FilterBar
            selectedType={travelType}
            onTypeChange={setTravelType}
            selectedRegion={region}
            onRegionChange={setRegion}
          />
        </div>

        <div className="mb-6 flex flex-col gap-4 border-t border-border pt-6 sm:flex-row sm:items-center sm:justify-between">
          <div className="flex items-center gap-4">
            <p className="text-sm text-secondary">
              {loading ? (
                'Searching...'
              ) : (
                <>
                  <span className="font-medium text-primary">{filteredAndSorted.length}</span>
                  {' '}destination{filteredAndSorted.length !== 1 ? 's' : ''} found
                </>
              )}
            </p>
            {hasActiveFilters && !loading && (
              <button
                type="button"
                onClick={handleClearFilters}
                className="text-sm font-medium text-accent hover:text-accent/80 transition-colors"
              >
                Clear filters
              </button>
            )}
          </div>

          <div className="flex items-center gap-4">
            <SortSelect value={sortBy} onChange={setSortBy} />
            <ViewToggle view={view} onChange={setView} />
          </div>
        </div>

        {error && (
          <ErrorState
            title="Failed to load destinations"
            description={error}
            onRetry={() => {
              setQuery('');
              setTravelType('all');
              setRegion('all');
            }}
          />
        )}

        {!error && loading && (
          <DestinationGridSkeleton count={6} />
        )}

        {!error && !loading && filteredAndSorted.length === 0 && (
          <EmptyState
            title="No destinations found"
            description="We couldn't find any destinations matching your search or filters. Try adjusting your criteria."
            actionLabel="Clear all filters"
            onAction={handleClearFilters}
          />
        )}

        {!error && !loading && filteredAndSorted.length > 0 && (
          <div
            className={
              view === 'grid'
                ? 'grid gap-6 sm:grid-cols-2 lg:grid-cols-3'
                : 'flex flex-col gap-4'
            }
            role="list"
            aria-label="Destinations"
          >
            {filteredAndSorted.map((destination) => (
              <div key={destination.id} role="listitem">
                <DestinationCard destination={destination} />
              </div>
            ))}
          </div>
        )}
      </PageContainer>
    </div>
  );
}
