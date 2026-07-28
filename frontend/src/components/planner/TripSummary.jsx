import Badge from '../common/Badge';
import { daysBetween, formatDateRange } from '../../utils/dateUtils';

export default function TripSummary({ tripData }) {
  const { destination, startDate, endDate, budget, travelers, theme } = tripData;

  const daysCount = daysBetween(startDate, endDate);

  return (
    <div className="rounded-card border border-border bg-surface p-6 shadow-card">
      <h3 className="mb-4 text-sm font-semibold uppercase tracking-wide text-primary">
        Trip Summary
      </h3>

      <div className="space-y-4">
        <div>
          <p className="text-xs text-secondary">Destination</p>
          <p className="mt-1 font-medium text-primary">
            {destination || 'Not selected'}
          </p>
        </div>

        <div>
          <p className="text-xs text-secondary">Dates</p>
          <p className="mt-1 font-medium text-primary">
            {formatDateRange(startDate, endDate)}
          </p>
          {daysCount > 0 && (
            <p className="text-xs text-secondary">{daysCount} day{daysCount !== 1 ? 's' : ''}</p>
          )}
        </div>

        <div>
          <p className="text-xs text-secondary">Budget</p>
          <p className="mt-1 font-medium text-primary">
            {budget || 'Not selected'}
          </p>
        </div>

        <div>
          <p className="text-xs text-secondary">Travelers</p>
          <p className="mt-1 font-medium text-primary">
            {travelers || 'Not selected'}
          </p>
        </div>

        <div>
          <p className="text-xs text-secondary">Theme</p>
          {theme ? (
            <Badge variant="accent">{theme}</Badge>
          ) : (
            <p className="mt-1 font-medium text-primary">Not selected</p>
          )}
        </div>
      </div>
    </div>
  );
}
