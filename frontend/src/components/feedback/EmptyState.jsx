import Button from '../common/Button';

export default function EmptyState({
  title = 'No destinations found',
  description = 'We couldn\'t find any destinations matching your search. Try adjusting your filters or search term.',
  actionLabel,
  actionTo,
  onAction,
}) {
  return (
    <div className="flex flex-col items-center justify-center py-16 text-center md:py-24">
      <div className="mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-background">
        <svg
          className="h-10 w-10 text-secondary/60"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={1.5}
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          />
        </svg>
      </div>

      <h3 className="mb-2 text-xl font-semibold text-primary">{title}</h3>
      <p className="mb-8 max-w-md text-secondary">{description}</p>

      {(actionLabel && actionTo) && (
        <Button variant="primary" to={actionTo}>
          {actionLabel}
        </Button>
      )}
      {(actionLabel && onAction) && (
        <Button variant="primary" onClick={onAction}>
          {actionLabel}
        </Button>
      )}
    </div>
  );
}
