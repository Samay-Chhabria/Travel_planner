import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Button from '../common/Button';

export default function SearchBar({
  placeholder = 'Where would you like to go?',
  defaultValue = '',
  className = '',
  size = 'lg',
  onSearch,
  mode = 'navigate',
}) {
  const [query, setQuery] = useState(defaultValue);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (event) => {
    event.preventDefault();
    const trimmed = query.trim();

    if (trimmed.length < 2) {
      setError('Please enter at least 2 characters to search.');
      return;
    }

    setError('');

    if (mode === 'controlled' && onSearch) {
      onSearch(trimmed);
    } else {
      navigate(`/explore?q=${encodeURIComponent(trimmed)}`);
    }
  };

  const handleChange = (event) => {
    const value = event.target.value;
    setQuery(value);
    if (error) setError('');

    if (mode === 'controlled' && onSearch) {
      onSearch(value);
    }
  };

  const sizeClasses = {
    lg: 'p-2 pl-5',
    md: 'p-1.5 pl-4',
  };

  return (
    <form
      onSubmit={handleSubmit}
      className={['w-full', className].filter(Boolean).join(' ')}
      role="search"
      aria-label="Search destinations"
    >
      <div
        className={[
          'flex flex-col gap-3 rounded-card border border-border bg-surface shadow-card sm:flex-row sm:items-center',
          sizeClasses[size],
        ].join(' ')}
      >
        <div className="flex flex-1 items-center gap-3">
          <svg
            className="h-5 w-5 shrink-0 text-secondary"
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
          <label htmlFor="destination-search" className="sr-only">
            Search destinations
          </label>
          <input
            id="destination-search"
            type="search"
            value={query}
            onChange={handleChange}
            placeholder={placeholder}
            autoComplete="off"
            className="min-h-[44px] w-full bg-transparent text-base text-primary placeholder:text-secondary focus:outline-none"
          />
        </div>
        <Button type="submit" variant="highlight" size="md" className="w-full sm:w-auto sm:shrink-0">
          Search
        </Button>
      </div>
      {error && (
        <p className="mt-2 text-sm text-highlight" role="alert">
          {error}
        </p>
      )}
    </form>
  );
}
