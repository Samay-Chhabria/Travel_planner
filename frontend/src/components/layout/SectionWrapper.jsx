import PageContainer from './PageContainer';

export default function SectionWrapper({
  children,
  id,
  className = '',
  background = 'default',
  ariaLabelledby,
}) {
  const backgrounds = {
    default: 'bg-background',
    surface: 'bg-surface',
    muted: 'bg-background/80',
  };

  return (
    <section
      id={id}
      aria-labelledby={ariaLabelledby}
      className={[backgrounds[background], 'py-16 md:py-24', className]
        .filter(Boolean)
        .join(' ')}
    >
      <PageContainer>{children}</PageContainer>
    </section>
  );
}
