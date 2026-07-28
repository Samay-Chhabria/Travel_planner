import { useCallback } from 'react';
import PageContainer from '../layout/PageContainer';
import useFetch from '../../hooks/useFetch';
import { getWeatherForDestination } from '../../services/weatherService';

function WeatherIcon({ condition }) {
  const c = condition?.toLowerCase() || '';
  const isRainy = c.includes('rain') || c.includes('drizzle');
  const isCloudy = c.includes('cloud') || c.includes('overcast');
  const isSnowy = c.includes('snow');

  if (isRainy) {
    return (
      <svg className="h-8 w-8 text-rain" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
      </svg>
    );
  }

  if (isSnowy) {
    return (
      <svg className="h-8 w-8 text-blue-300" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 3v1m0 16v1m9-9h-1M4 12H3m3.343-5.657L7.05 6.05m10.607-1.414l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
      </svg>
    );
  }

  if (isCloudy) {
    return (
      <svg className="h-8 w-8 text-secondary" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z" />
      </svg>
    );
  }

  return (
    <svg className="h-8 w-8 text-star" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
    </svg>
  );
}

function WeatherSkeleton() {
  return (
    <div className="grid gap-6 md:grid-cols-2" aria-label="Loading weather" role="status">
      <div className="rounded-card border border-border bg-surface p-6 shadow-card animate-pulse">
        <div className="flex items-center gap-4">
          <div className="h-8 w-8 rounded bg-border/60" />
          <div>
            <div className="h-8 w-16 rounded bg-border/60" />
            <div className="mt-1 h-4 w-12 rounded bg-border/40" />
          </div>
        </div>
        <div className="mt-4 h-5 w-24 rounded bg-border/40" />
        <div className="mt-1 h-4 w-40 rounded bg-border/40" />
      </div>
      <div className="rounded-card border border-border bg-surface p-6 shadow-card animate-pulse">
        <div className="mb-4 h-4 w-28 rounded bg-border/40" />
        <div className="space-y-3">
          {Array.from({ length: 5 }).map((_, i) => (
            <div key={i} className="flex items-center justify-between">
              <div className="h-4 w-10 rounded bg-border/40" />
              <div className="h-8 w-8 rounded bg-border/40" />
              <div className="h-4 w-16 rounded bg-border/40" />
              <div className="h-4 w-16 rounded bg-border/40" />
            </div>
          ))}
        </div>
      </div>
      <span className="sr-only">Loading weather data...</span>
    </div>
  );
}

function formatForecastDate(dateStr) {
  try {
    const date = new Date(dateStr + 'T00:00:00');
    return date.toLocaleDateString('en-US', { weekday: 'short' });
  } catch {
    return dateStr;
  }
}

export default function WeatherWidget({ destinationId }) {
  const fetchWeather = useCallback(
    () => getWeatherForDestination(destinationId),
    [destinationId],
  );

  const { data: weather, loading, error, execute: retry } = useFetch(
    fetchWeather,
    [destinationId],
  );

  return (
    <section className="bg-background py-12 md:py-16" aria-labelledby="weather-heading">
      <PageContainer>
        <p className="mb-2 text-sm font-medium uppercase tracking-widest text-accent">
          Weather
        </p>
        <h2 id="weather-heading" className="text-2xl font-bold text-primary md:text-3xl">
          Current conditions
        </h2>

        <div className="mt-8">
          {loading && <WeatherSkeleton />}

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
                Weather data unavailable
              </h3>
              <p className="mb-6 max-w-sm text-secondary">
                {error || 'Unable to load weather information for this destination.'}
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

          {!loading && !error && !weather && (
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
                    d="M3 15a4 4 0 004 4h9a5 5 0 10-.1-9.999 5.002 5.002 0 10-9.78 2.096A4.001 4.001 0 003 15z"
                  />
                </svg>
              </div>
              <h3 className="mb-2 text-lg font-semibold text-primary">
                No weather data
              </h3>
              <p className="max-w-sm text-secondary">
                Weather information is not available for this destination yet.
              </p>
            </div>
          )}

          {!loading && !error && weather && (
            <div className="grid gap-6 md:grid-cols-2">
              <div className="rounded-card border border-border bg-surface p-6 shadow-card">
                <div className="flex items-center gap-4">
                  <WeatherIcon condition={weather.current.condition} />
                  <div>
                    <p className="text-3xl font-bold text-primary">
                      {weather.current.temperature_c}°C
                    </p>
                    <p className="text-sm text-secondary">
                      {weather.current.temperature_f}°F
                    </p>
                  </div>
                </div>
                <p className="mt-4 font-medium text-primary">{weather.current.condition}</p>
                <p className="text-sm text-secondary">{weather.current.description}</p>
              </div>

              <div className="rounded-card border border-border bg-surface p-6 shadow-card">
                <h3 className="mb-4 text-sm font-semibold text-primary">
                  {weather.forecast.length}-Day Forecast
                </h3>
                <div className="space-y-3">
                  {weather.forecast.map((day) => (
                    <div key={day.date} className="flex items-center justify-between">
                      <span className="w-12 text-sm font-medium text-primary">
                        {formatForecastDate(day.date)}
                      </span>
                      <WeatherIcon condition={day.condition} />
                      <span className="text-sm text-secondary">{day.condition}</span>
                      <span className="text-sm font-medium text-primary">
                        {day.max_temp_c}° / {day.min_temp_c}°
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}
        </div>
      </PageContainer>
    </section>
  );
}
