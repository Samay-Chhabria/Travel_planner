export default function SectionHeader({ eyebrow, title, description, id, centered = false }) {
  return (
    <div className={centered ? 'text-center mb-8' : 'mb-8'}>
      {eyebrow && (
        <p className="mb-2 text-sm font-medium uppercase tracking-widest text-accent">
          {eyebrow}
        </p>
      )}
      <h2
        id={id ? `${id}-heading` : undefined}
        className="text-2xl font-bold text-primary md:text-3xl"
      >
        {title}
      </h2>
      {description && (
        <p className="mt-3 text-secondary">
          {description}
        </p>
      )}
    </div>
  );
}
