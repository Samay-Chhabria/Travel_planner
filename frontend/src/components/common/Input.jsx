export default function Input({
  label,
  name,
  type = 'text',
  placeholder,
  required = false,
  error,
  value,
  onChange,
  as: Component = 'input',
  rows = 4,
  className = '',
  ...props
}) {
  const fieldId = `field-${name}`;
  const errorId = error ? `${fieldId}-error` : undefined;

  return (
    <div className={className}>
      <label
        htmlFor={fieldId}
        className="mb-2 block text-sm font-medium text-primary"
      >
        {label}
        {required && <span className="ml-1 text-highlight">*</span>}
      </label>

      <Component
        id={fieldId}
        name={name}
        type={type}
        placeholder={placeholder}
        required={required}
        value={value}
        onChange={onChange}
        rows={Component === 'textarea' ? rows : undefined}
        aria-invalid={error ? 'true' : undefined}
        aria-describedby={errorId}
        className={[
          'w-full rounded-card border bg-surface px-4 py-3 text-sm text-primary',
          'placeholder:text-secondary transition-colors duration-200',
          'hover:border-accent/40 focus:border-accent focus:outline-none focus:ring-2 focus:ring-accent/20',
          error
            ? 'border-error'
            : 'border-border',
        ].join(' ')}
        {...props}
      />

      {error && (
        <p id={errorId} className="mt-1.5 text-xs text-error" role="alert">
          {error}
        </p>
      )}
    </div>
  );
}
