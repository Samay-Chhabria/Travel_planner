export default function CardSkeleton({ className = '' }) {
  return (
    <div
      className={[
        'animate-pulse overflow-hidden rounded-card border border-border bg-surface',
        className,
      ]
        .filter(Boolean)
        .join(' ')}
      aria-hidden="true"
    >
      <div className="aspect-[4/3] bg-border/60" />
      <div className="space-y-3 p-5 md:p-6">
        <div className="h-5 w-2/3 rounded bg-border/60" />
        <div className="h-4 w-1/2 rounded bg-border/40" />
        <div className="h-4 w-full rounded bg-border/40" />
        <div className="h-4 w-5/6 rounded bg-border/40" />
      </div>
    </div>
  );
}

export function DestinationGridSkeleton({ count = 6 }) {
  return (
    <div
      className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3"
      aria-label="Loading destinations"
      role="status"
    >
      {Array.from({ length: count }).map((_, index) => (
        <CardSkeleton key={index} />
      ))}
      <span className="sr-only">Loading featured destinations...</span>
    </div>
  );
}
