const TRAVELER_OPTIONS = [
  { id: 'solo', label: 'Solo', icon: '👤', description: '1 traveler' },
  { id: 'couple', label: 'Couple', icon: '👫', description: '2 travelers' },
  { id: 'family', label: 'Family', icon: '👨‍👩‍👧‍👦', description: '3-5 travelers' },
  { id: 'group', label: 'Group', icon: '👥', description: '6+ travelers' },
];

export default function TravelersSelector({ selected, onSelect }) {
  return (
    <div className="space-y-4">
      <h3 className="text-sm font-semibold text-primary">Travelers</h3>

      <div className="grid grid-cols-2 gap-3 sm:grid-cols-4">
        {TRAVELER_OPTIONS.map((option) => (
          <button
            key={option.id}
            type="button"
            onClick={() => onSelect(option.id)}
            className={[
              'flex flex-col items-center rounded-card border p-4 text-center transition-all duration-200',
              'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2',
              selected === option.id
                ? 'border-accent bg-accent/5 shadow-sm'
                : 'border-border bg-surface hover:border-accent/40',
            ].join(' ')}
            aria-pressed={selected === option.id}
          >
            <span className="mb-2 text-2xl" aria-hidden="true">{option.icon}</span>
            <span className="font-medium text-primary">{option.label}</span>
            <span className="mt-1 text-xs text-secondary">{option.description}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
