export default function DatePicker({ startDate, endDate, onStartChange, onEndChange }) {
  return (
    <div className="space-y-4">
      <h3 className="text-sm font-semibold text-primary">Travel Dates</h3>

      <div className="grid gap-4 sm:grid-cols-2">
        <div>
          <label
            htmlFor="start-date"
            className="mb-2 block text-sm text-secondary"
          >
            Start date
          </label>
          <input
            id="start-date"
            type="date"
            value={startDate}
            onChange={(e) => onStartChange(e.target.value)}
            min={new Date().toISOString().split('T')[0]}
            className={[
              'w-full rounded-card border border-border bg-surface px-4 py-3 text-sm text-primary',
              'transition-colors duration-200 hover:border-accent/40',
              'focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/20',
            ].join(' ')}
          />
        </div>

        <div>
          <label
            htmlFor="end-date"
            className="mb-2 block text-sm text-secondary"
          >
            End date
          </label>
          <input
            id="end-date"
            type="date"
            value={endDate}
            onChange={(e) => onEndChange(e.target.value)}
            min={startDate || new Date().toISOString().split('T')[0]}
            className={[
              'w-full rounded-card border border-border bg-surface px-4 py-3 text-sm text-primary',
              'transition-colors duration-200 hover:border-accent/40',
              'focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/20',
            ].join(' ')}
          />
        </div>
      </div>

      {startDate && endDate && (
        <p className="text-xs text-secondary">
          {Math.ceil((new Date(endDate) - new Date(startDate)) / (1000 * 60 * 60 * 24)) + 1} day trip
        </p>
      )}
    </div>
  );
}
