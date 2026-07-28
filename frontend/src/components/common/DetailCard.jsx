import Badge from './Badge';
import StarRating from './StarRating';
import PriceLevel from './PriceLevel';

export default function DetailCard({ image, imageAlt, badge, title, description, rating, priceLevel, variant = 'default' }) {
  return (
    <article
      className={[
        'group flex flex-col overflow-hidden rounded-card border border-border shadow-card',
        'transition-all duration-300 hover:-translate-y-1 hover:shadow-card-hover',
        variant === 'default' ? 'bg-background' : 'bg-surface',
      ].join(' ')}
    >
      <div className="relative aspect-[4/3] overflow-hidden">
        <img
          src={image}
          alt={imageAlt}
          className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
          loading="lazy"
        />
        {badge && (
          <div className="absolute left-3 top-3">
            <Badge variant="accent">{badge}</Badge>
          </div>
        )}
      </div>

      <div className="flex flex-1 flex-col p-4">
        <div className="flex items-start justify-between gap-2">
          <h3 className="font-semibold text-primary">{title}</h3>
          {priceLevel && <PriceLevel price={priceLevel} />}
        </div>
        <p className="mt-1 flex-1 text-sm text-secondary line-clamp-2">
          {description}
        </p>
        {rating != null && (
          <div className="mt-3">
            <StarRating rating={rating} />
          </div>
        )}
      </div>
    </article>
  );
}
