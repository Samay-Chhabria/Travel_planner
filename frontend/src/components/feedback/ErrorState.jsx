import Button from '../common/Button';

export default function ErrorState({
  title = 'Something went wrong',
  description = 'We encountered an error while loading destinations. Please try again.',
  onRetry,
}) {
  return (
    <div className="flex flex-col items-center justify-center py-16 text-center md:py-24">
      <div className="mb-6 flex h-20 w-20 items-center justify-center rounded-full bg-highlight/10">
        <svg
          className="h-10 w-10 text-highlight"
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={1.5}
            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
          />
        </svg>
      </div>

      <h3 className="mb-2 text-xl font-semibold text-primary">{title}</h3>
      <p className="mb-8 max-w-md text-secondary">{description}</p>

      {onRetry && (
        <Button variant="primary" onClick={onRetry}>
          Try Again
        </Button>
      )}
    </div>
  );
}
