import { useState } from 'react';
import { Link } from 'react-router-dom';
import Badge from '../common/Badge';

const FALLBACK_IMAGE =
  'https://images.unsplash.com/photo-1488646953014-85cb44e25828?w=800&q=80';

export default function DestinationCard({ destination }) {
  const {
    id,
    slug,
    name,
    country,
    region,
    description,
    image_url: imageUrl,
    highlights = [],
    best_time_to_visit: bestTime,
    travel_type: travelType,
  } = destination;

  const [imgSrc, setImgSrc] = useState(imageUrl || FALLBACK_IMAGE);

  const handleImageError = () => {
    if (imgSrc !== FALLBACK_IMAGE) {
      setImgSrc(FALLBACK_IMAGE);
    }
  };

  const destinationPath = `/destinations/${slug || id}`;

  return (
    <article className="group flex h-full flex-col overflow-hidden rounded-card border border-border bg-surface shadow-card transition-all duration-300 hover:-translate-y-1 hover:shadow-card-hover">
      <Link to={destinationPath} className="relative block aspect-[4/3] overflow-hidden">
        <img
          src={imgSrc}
          alt={`${name}, ${country}`}
          className="h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
          loading="lazy"
          onError={handleImageError}
        />
        {travelType && (
          <div className="absolute left-4 top-4">
            <Badge variant="accent">{travelType}</Badge>
          </div>
        )}
      </Link>

      <div className="flex flex-1 flex-col p-5 md:p-6">
        <div className="mb-2 flex items-start justify-between gap-3">
          <div>
            <h3 className="text-lg font-semibold text-primary">
              <Link
                to={destinationPath}
                className="transition-colors hover:text-accent focus-visible:text-accent"
              >
                {name}
              </Link>
            </h3>
            <p className="mt-1 text-sm text-secondary">
              {region ? `${region} · ${country}` : country}
            </p>
          </div>
        </div>

        <p className="mb-4 line-clamp-2 flex-1 text-sm leading-relaxed text-secondary">
          {description}
        </p>

        {highlights.length > 0 && (
          <ul className="mb-4 flex flex-wrap gap-2" aria-label="Highlights">
            {highlights.slice(0, 3).map((highlight) => (
              <li key={highlight}>
                <Badge>{highlight}</Badge>
              </li>
            ))}
          </ul>
        )}

        {bestTime && (
          <p className="mt-auto text-xs text-secondary">
            Best time to visit:{' '}
            <span className="font-medium text-primary">{bestTime}</span>
          </p>
        )}
      </div>
    </article>
  );
}
