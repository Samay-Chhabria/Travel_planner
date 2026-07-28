import { Link } from 'react-router-dom';

const variantStyles = {
  primary:
    'bg-accent text-white hover:bg-accent/90 focus-visible:ring-accent/40 shadow-sm',
  secondary:
    'bg-surface text-primary border border-border hover:bg-background focus-visible:ring-accent/30',
  highlight:
    'bg-highlight text-white hover:bg-highlight/90 focus-visible:ring-highlight/40 shadow-sm',
  ghost:
    'bg-transparent text-primary hover:bg-background focus-visible:ring-accent/30',
};

const sizeStyles = {
  sm: 'px-4 py-2 text-sm',
  md: 'px-6 py-3 text-base',
  lg: 'px-8 py-3.5 text-base',
};

function getButtonClasses({ variant, size, className }) {
  return [
    'inline-flex min-h-[44px] items-center justify-center gap-2 rounded-pill font-medium',
    'transition-all duration-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2',
    'disabled:cursor-not-allowed disabled:opacity-50',
    variantStyles[variant],
    sizeStyles[size],
    className,
  ]
    .filter(Boolean)
    .join(' ');
}

export default function Button({
  children,
  variant = 'primary',
  size = 'md',
  type = 'button',
  disabled = false,
  loading = false,
  className = '',
  to,
  ...props
}) {
  const classes = getButtonClasses({ variant, size, className });

  const content = (
    <>
      {loading && (
        <span
          className="h-4 w-4 animate-spin rounded-full border-2 border-current border-t-transparent"
          aria-hidden="true"
        />
      )}
      {children}
    </>
  );

  if (to) {
    return (
      <Link to={to} className={classes} {...props}>
        {content}
      </Link>
    );
  }

  return (
    <button
      type={type}
      disabled={disabled || loading}
      className={classes}
      {...props}
    >
      {content}
    </button>
  );
}
