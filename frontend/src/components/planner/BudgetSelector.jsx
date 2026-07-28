const BUDGET_OPTIONS = [
  {
    id: 'budget',
    label: 'Budget',
    description: 'Affordable stays and free activities',
    icon: '$',
  },
  {
    id: 'moderate',
    label: 'Moderate',
    description: 'Comfortable mid-range options',
    icon: '$$',
  },
  {
    id: 'luxury',
    label: 'Luxury',
    description: 'Premium experiences and accommodations',
    icon: '$$$',
  },
];

export default function BudgetSelector({ selected, onSelect }) {
  return (
    <div className="space-y-4">
      <h3 className="text-sm font-semibold text-primary">Budget Level</h3>

      <div className="grid gap-3 sm:grid-cols-3">
        {BUDGET_OPTIONS.map((option) => (
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
            <span className="mb-2 text-lg font-bold text-accent">{option.icon}</span>
            <span className="font-medium text-primary">{option.label}</span>
            <span className="mt-1 text-xs text-secondary">{option.description}</span>
          </button>
        ))}
      </div>
    </div>
  );
}
