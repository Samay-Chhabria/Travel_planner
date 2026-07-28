import Button from '../common/Button';
import Badge from '../common/Badge';
import { daysBetween } from '../../utils/dateUtils';

function ItinerarySkeleton() {
  return (
    <div className="space-y-6 animate-pulse" role="status" aria-label="Generating itinerary">
      <div className="rounded-card border border-border bg-background p-6">
        <div className="h-6 w-48 rounded bg-border/60" />
        <div className="mt-3 h-4 w-full rounded bg-border/40" />
        <div className="mt-2 h-4 w-3/4 rounded bg-border/40" />
        <div className="mt-4 flex gap-2">
          <div className="h-6 w-16 rounded bg-border/40" />
          <div className="h-6 w-20 rounded bg-border/40" />
          <div className="h-6 w-14 rounded bg-border/40" />
          <div className="h-6 w-18 rounded bg-border/40" />
        </div>
      </div>
      {Array.from({ length: 3 }).map((_, i) => (
        <div key={i} className="border-l-2 border-border/40 pl-4 space-y-2">
          <div className="h-5 w-40 rounded bg-border/40" />
          <div className="h-4 w-full rounded bg-border/30" />
          <div className="h-4 w-5/6 rounded bg-border/30" />
          <div className="h-4 w-2/3 rounded bg-border/30" />
        </div>
      ))}
      <span className="sr-only">Generating your trip plan...</span>
    </div>
  );
}

function formatDate(dateStr) {
  try {
    return new Date(dateStr + 'T00:00:00').toLocaleDateString('en-US', {
      weekday: 'short',
      month: 'short',
      day: 'numeric',
    });
  } catch {
    return dateStr;
  }
}

export default function ItineraryPlaceholder({ tripData, plan, loading, onGenerate }) {
  if (loading) {
    return <ItinerarySkeleton />;
  }

  if (!plan) {
    const allFieldsFilled =
      tripData.destination &&
      tripData.startDate &&
      tripData.endDate &&
      tripData.budget &&
      tripData.travelers &&
      tripData.theme;

    return (
      <div className="rounded-card border border-dashed border-border bg-background p-8 text-center">
        <div className="mb-4 inline-flex h-16 w-16 items-center justify-center rounded-full bg-accent/10">
          <svg className="h-8 w-8 text-accent" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-3 7h3m-3 4h3m-6-4h.01M9 16h.01" />
          </svg>
        </div>

        <h3 className="mb-2 text-lg font-semibold text-primary">
          Your itinerary awaits
        </h3>
        <p className="mb-6 max-w-md mx-auto text-sm text-secondary">
          Fill in all the trip details and click &quot;Generate Itinerary&quot; to see a personalized travel plan.
        </p>

        <Button variant="highlight" size="lg" onClick={onGenerate} disabled={!allFieldsFilled}>
          Generate Itinerary
        </Button>

        {!allFieldsFilled && (
          <p className="mt-3 text-xs text-secondary">
            Complete all fields above to enable itinerary generation
          </p>
        )}
      </div>
    );
  }

  const totalDays = plan.duration_days || daysBetween(tripData.startDate, tripData.endDate);

  return (
    <div className="space-y-6">
      <div className="rounded-card border border-accent/20 bg-accent/5 p-4">
        <div className="flex items-center gap-2">
          <svg className="h-5 w-5 text-accent" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
          </svg>
          <p className="text-sm font-medium text-accent">Itinerary generated successfully!</p>
        </div>
      </div>

      <div className="rounded-card border border-border bg-surface p-6">
        <h3 className="mb-2 text-lg font-semibold text-primary">
          {plan.destination}{plan.country ? `, ${plan.country}` : ''} Trip Plan
        </h3>
        <p className="mb-4 text-sm text-secondary">
          {plan.summary}
        </p>

        <div className="flex flex-wrap gap-2 mb-6">
          <Badge variant="default">{totalDays} days</Badge>
          {plan.budget_level && <Badge variant="default">{plan.budget_level}</Badge>}
          {plan.group_type && <Badge variant="default">{plan.group_type}</Badge>}
          {plan.travel_style && <Badge variant="default">{plan.travel_style}</Badge>}
        </div>

        {plan.weather_summary && (
          <div className="mb-6 rounded-card border border-border bg-background p-4">
            <h4 className="mb-1 text-sm font-semibold text-primary">Weather Outlook</h4>
            <p className="text-sm text-secondary">{plan.weather_summary}</p>
          </div>
        )}

        <div className="space-y-4">
          {plan.days.map((day) => (
            <div key={day.day} className="border-l-2 border-accent pl-4">
              <h4 className="font-medium text-primary">
                Day {day.day}: {day.title}
                {day.date && (
                  <span className="ml-2 text-xs font-normal text-secondary">
                    {formatDate(day.date)}
                  </span>
                )}
              </h4>
              <ul className="mt-2 space-y-1">
                {day.activities.map((activity, i) => (
                  <li key={i} className="flex items-start gap-2 text-sm text-secondary">
                    {activity.time && (
                      <span className="shrink-0 text-xs font-medium text-accent">
                        {activity.time}
                      </span>
                    )}
                    <span className="mt-1 h-1.5 w-1.5 shrink-0 rounded-full bg-accent" aria-hidden="true" />
                    {activity.description}
                  </li>
                ))}
              </ul>
              {day.notes && (
                <p className="mt-2 text-xs text-secondary italic">{day.notes}</p>
              )}
            </div>
          ))}
        </div>

        {(plan.top_attractions?.length > 0 ||
          plan.recommended_hotels?.length > 0 ||
          plan.recommended_restaurants?.length > 0) && (
          <div className="mt-6 grid gap-4 sm:grid-cols-3">
            {plan.top_attractions?.length > 0 && (
              <div>
                <h4 className="mb-2 text-sm font-semibold text-primary">Top Attractions</h4>
                <ul className="space-y-1">
                  {plan.top_attractions.map((name, i) => (
                    <li key={i} className="text-xs text-secondary">· {name}</li>
                  ))}
                </ul>
              </div>
            )}
            {plan.recommended_hotels?.length > 0 && (
              <div>
                <h4 className="mb-2 text-sm font-semibold text-primary">Recommended Hotels</h4>
                <ul className="space-y-1">
                  {plan.recommended_hotels.map((name, i) => (
                    <li key={i} className="text-xs text-secondary">· {name}</li>
                  ))}
                </ul>
              </div>
            )}
            {plan.recommended_restaurants?.length > 0 && (
              <div>
                <h4 className="mb-2 text-sm font-semibold text-primary">Recommended Restaurants</h4>
                <ul className="space-y-1">
                  {plan.recommended_restaurants.map((name, i) => (
                    <li key={i} className="text-xs text-secondary">· {name}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}
