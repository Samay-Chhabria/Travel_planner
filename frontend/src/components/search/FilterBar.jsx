const TRAVEL_TYPES = [
  { id: 'all', label: 'All Types' },
  { id: 'City', label: 'City' },
  { id: 'Beach', label: 'Beach' },
  { id: 'Adventure', label: 'Adventure' },
  { id: 'Nature', label: 'Nature' },
  { id: 'Culture', label: 'Culture' },
];

const REGIONS = [
  { id: 'all', label: 'All Regions' },
  { id: 'Europe', label: 'Europe' },
  { id: 'Asia', label: 'Asia' },
  { id: 'North America', label: 'North America' },
  { id: 'South America', label: 'South America' },
  { id: 'Africa', label: 'Africa' },
  { id: 'Oceania', label: 'Oceania' },
];

export default function FilterBar({
  selectedType,
  onTypeChange,
  selectedRegion,
  onRegionChange,
}) {
  return (
    <div className="space-y-4">
      <div>
        <h3 className="mb-3 text-sm font-medium text-primary">Travel Type</h3>
        <div className="flex flex-wrap gap-2" role="group" aria-label="Filter by travel type">
          {TRAVEL_TYPES.map((type) => (
            <button
              key={type.id}
              type="button"
              onClick={() => onTypeChange(type.id)}
              className={[
                'rounded-pill px-4 py-2 text-sm font-medium transition-all duration-200',
                'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2',
                selectedType === type.id
                  ? 'bg-accent text-white shadow-sm'
                  : 'bg-surface text-secondary border border-border hover:border-accent/40 hover:text-primary',
              ].join(' ')}
              aria-pressed={selectedType === type.id}
            >
              {type.label}
            </button>
          ))}
        </div>
      </div>

      <div>
        <h3 className="mb-3 text-sm font-medium text-primary">Region</h3>
        <div className="flex flex-wrap gap-2" role="group" aria-label="Filter by region">
          {REGIONS.map((region) => (
            <button
              key={region.id}
              type="button"
              onClick={() => onRegionChange(region.id)}
              className={[
                'rounded-pill px-4 py-2 text-sm font-medium transition-all duration-200',
                'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2',
                selectedRegion === region.id
                  ? 'bg-accent text-white shadow-sm'
                  : 'bg-surface text-secondary border border-border hover:border-accent/40 hover:text-primary',
              ].join(' ')}
              aria-pressed={selectedRegion === region.id}
            >
              {region.label}
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
