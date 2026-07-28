export default function Badge({ children, variant = 'default', className = '' }) {
  const variants = {
    default: 'bg-background text-secondary border border-border',
    accent: 'bg-accent/10 text-accent border border-accent/20',
    highlight: 'bg-highlight/10 text-highlight border border-highlight/20',
  };

  return (
    <span
      className={[
        'inline-flex items-center rounded-pill px-3 py-1 text-xs font-medium',
        variants[variant],
        className,
      ]
        .filter(Boolean)
        .join(' ')}
    >
      {children}
    </span>
  );
}
