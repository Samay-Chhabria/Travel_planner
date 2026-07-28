import Badge from '../common/Badge';
import { POPULAR_THEMES } from '../../utils/constants';

export default function ThemeSelector({ selected, onSelect }) {
  return (
    <div className="space-y-4">
      <h3 className="text-sm font-semibold text-primary">Travel Theme</h3>

      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {POPULAR_THEMES.map((theme) => (
          <button
            key={theme.id}
            type="button"
            onClick={() => onSelect(theme.id)}
            className={[
              'group relative overflow-hidden rounded-card border text-left transition-all duration-200',
              'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2',
              selected === theme.id
                ? 'border-accent shadow-sm ring-1 ring-accent/20'
                : 'border-border hover:border-accent/40',
            ].join(' ')}
            aria-pressed={selected === theme.id}
          >
            <div className="relative aspect-[3/2] overflow-hidden">
              <img
                src={theme.imageUrl}
                alt={`${theme.title} theme`}
                className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
                loading="lazy"
              />
              <div className="absolute inset-0 bg-gradient-to-t from-primary/60 to-transparent" aria-hidden="true" />
              <div className="absolute bottom-3 left-3 right-3">
                <Badge variant="highlight" className="mb-1 bg-highlight/20 text-white border-white/20">
                  {theme.tag}
                </Badge>
                <h4 className="text-sm font-semibold text-white">{theme.title}</h4>
              </div>
            </div>
          </button>
        ))}
      </div>
    </div>
  );
}
