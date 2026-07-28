const SORT_OPTIONS = [
  { value: 'name-asc', label: 'Name (A-Z)' },
  { value: 'name-desc', label: 'Name (Z-A)' },
  { value: 'region', label: 'Region' },
  { value: 'travel_type', label: 'Travel Type' },
];

export default function SortSelect({ value, onChange }) {
  return (
    <div className="flex items-center gap-3">
      <label
        htmlFor="sort-select"
        className="text-sm font-medium text-secondary whitespace-nowrap"
      >
        Sort by
      </label>
      <select
        id="sort-select"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className={[
          'min-h-[44px] rounded-pill border border-border bg-surface px-4 py-2 pr-10 text-sm font-medium text-primary',
          'transition-colors duration-200 hover:border-accent/40',
          'focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/20',
          'cursor-pointer appearance-none',
          'bg-[url("data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' fill=\'none\' viewBox=\'0 0 24 24\' stroke=\'%23717171\'%3E%3Cpath stroke-linecap=\'round\' stroke-linejoin=\'round\' stroke-width=\'2\' d=\'M19 9l-7 7-7-7\'/%3E%3C/svg%3E")]',
          'bg-[length:20px] bg-[right_12px_center] bg-no-repeat',
        ].join(' ')}
      >
        {SORT_OPTIONS.map((option) => (
          <option key={option.value} value={option.value}>
            {option.label}
          </option>
        ))}
      </select>
    </div>
  );
}
