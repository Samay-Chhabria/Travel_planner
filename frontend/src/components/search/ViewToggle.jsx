export default function ViewToggle({ view, onChange }) {
  return (
    <div
      className="inline-flex rounded-pill border border-border bg-surface p-1"
      role="group"
      aria-label="View mode"
    >
      <button
        type="button"
        onClick={() => onChange('grid')}
        className={[
          'inline-flex items-center justify-center gap-2 rounded-pill px-3 py-2 text-sm font-medium transition-all duration-200',
          'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2',
          view === 'grid'
            ? 'bg-accent text-white shadow-sm'
            : 'text-secondary hover:text-primary',
        ].join(' ')}
        aria-pressed={view === 'grid'}
        aria-label="Grid view"
      >
        <svg
          className="h-5 w-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zm10 0a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zm10 0a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"
          />
        </svg>
        <span className="hidden sm:inline">Grid</span>
      </button>

      <button
        type="button"
        onClick={() => onChange('list')}
        className={[
          'inline-flex items-center justify-center gap-2 rounded-pill px-3 py-2 text-sm font-medium transition-all duration-200',
          'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2',
          view === 'list'
            ? 'bg-accent text-white shadow-sm'
            : 'text-secondary hover:text-primary',
        ].join(' ')}
        aria-pressed={view === 'list'}
        aria-label="List view"
      >
        <svg
          className="h-5 w-5"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M4 6h16M4 12h16M4 18h16"
          />
        </svg>
        <span className="hidden sm:inline">List</span>
      </button>
    </div>
  );
}
