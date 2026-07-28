import { useState, useMemo } from 'react';
import { ALL_DESTINATIONS } from '../../utils/constants';

export default function DestinationSelector({ selected, onSelect }) {
  const [searchQuery, setSearchQuery] = useState('');

  const filteredDestinations = useMemo(() => {
    const query = searchQuery.toLowerCase();
    return ALL_DESTINATIONS.filter((d) => (
      d.name.toLowerCase().includes(query) ||
      d.country.toLowerCase().includes(query) ||
      d.region.toLowerCase().includes(query)
    ));
  }, [searchQuery]);

  return (
    <div className="space-y-4">
      <h3 className="text-sm font-semibold text-primary">Destination</h3>

      <div className="relative">
        <svg
          className="absolute left-4 top-1/2 h-5 w-5 -translate-y-1/2 text-secondary"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          />
        </svg>
        <input
          type="search"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          placeholder="Search destinations..."
          aria-label="Search destinations"
          className={[
            'w-full rounded-card border border-border bg-surface py-3 pl-11 pr-4 text-sm text-primary',
            'placeholder:text-secondary transition-colors duration-200 hover:border-accent/40',
            'focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/20',
          ].join(' ')}
        />
      </div>

      <div className="max-h-64 overflow-y-auto rounded-card border border-border">
        {filteredDestinations.length === 0 ? (
          <p className="p-4 text-center text-sm text-secondary">
            No destinations found
          </p>
        ) : (
          <ul className="divide-y divide-border" role="listbox" aria-label="Select destination">
            {filteredDestinations.map((dest) => (
              <li key={dest.id}>
                <button
                  type="button"
                  onClick={() => onSelect(dest.name)}
                  className={[
                    'flex w-full items-center gap-3 px-4 py-3 text-left transition-colors duration-150',
                    'hover:bg-background focus-visible:bg-background focus-visible:outline-none',
                    selected === dest.name && 'bg-accent/5',
                  ].join(' ')}
                  role="option"
                  aria-selected={selected === dest.name}
                >
                   <img
                    src={dest.image_url}
                    alt={`${dest.name} destination`}
                    className="h-10 w-10 rounded-lg object-cover"
                    loading="lazy"
                  />
                  <div className="flex-1 min-w-0">
                    <p className="font-medium text-primary truncate">{dest.name}</p>
                    <p className="text-xs text-secondary truncate">
                      {dest.region} · {dest.country}
                    </p>
                  </div>
                  {selected === dest.name && (
                    <svg className="h-5 w-5 shrink-0 text-accent" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                      <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                    </svg>
                  )}
                </button>
              </li>
            ))}
          </ul>
        )}
      </div>

      {selected && (
        <p className="text-sm text-secondary">
          Selected: <span className="font-medium text-primary">{selected}</span>
        </p>
      )}
    </div>
  );
}
