import SectionWrapper from '../layout/SectionWrapper';
import ThemeCard from '../cards/ThemeCard';
import { POPULAR_THEMES } from '../../utils/constants';

export default function PopularThemes() {
  return (
    <SectionWrapper
      id="themes"
      background="surface"
      ariaLabelledby="themes-heading"
    >
      <div className="mx-auto mb-10 max-w-2xl text-center md:mb-12">
        <p className="mb-2 text-sm font-medium uppercase tracking-widest text-accent">
          Find your vibe
        </p>
        <h2 id="themes-heading" className="text-3xl font-bold text-primary md:text-4xl">
          Popular travel themes
        </h2>
        <p className="mt-3 text-secondary md:text-lg">
          Browse by mood and interest to discover destinations that match the way
          you love to travel.
        </p>
      </div>

      <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {POPULAR_THEMES.map((theme) => (
          <ThemeCard key={theme.id} theme={theme} />
        ))}
      </div>
    </SectionWrapper>
  );
}
