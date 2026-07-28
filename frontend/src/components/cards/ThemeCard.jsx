import { Link } from 'react-router-dom';
import Badge from '../common/Badge';

export default function ThemeCard({ theme }) {
  const { id, title, description, imageUrl, tag } = theme;

  return (
    <article className="group relative overflow-hidden rounded-card shadow-card transition-all duration-300 hover:-translate-y-1 hover:shadow-card-hover">
      <Link
        to={`/explore?theme=${id}`}
        className="block aspect-[3/4] sm:aspect-[4/5]"
        aria-label={`Explore ${title} destinations`}
      >
        <img
          src={imageUrl}
          alt={`${title} travel theme`}
          className="absolute inset-0 h-full w-full object-cover transition-transform duration-500 group-hover:scale-105"
          loading="lazy"
        />
        <div
          className="absolute inset-0 bg-gradient-to-t from-primary/80 via-primary/30 to-transparent"
          aria-hidden="true"
        />
        <div className="absolute inset-x-0 bottom-0 p-5 md:p-6">
          {tag && (
            <Badge variant="highlight" className="mb-3 bg-highlight/20 text-white border-white/20">
              {tag}
            </Badge>
          )}
          <h3 className="text-xl font-semibold text-white md:text-2xl">{title}</h3>
          <p className="mt-2 text-sm text-white/85 line-clamp-2">{description}</p>
        </div>
      </Link>
    </article>
  );
}
