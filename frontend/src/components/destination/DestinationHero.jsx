import { Link } from 'react-router-dom';
import Badge from '../common/Badge';
import PageContainer from '../layout/PageContainer';

export default function DestinationHero({ destination }) {
  const { name, country, region, image_url: imageUrl, description, travel_type: travelType } = destination;

  return (
    <section className="relative overflow-hidden bg-primary" aria-labelledby="dest-hero-heading">
      <div className="absolute inset-0" aria-hidden="true">
        <img
          src={imageUrl}
          alt={`${name}, ${country}`}
          className="h-full w-full object-cover opacity-50"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-primary/90 via-primary/50 to-primary/30" />
      </div>

      <PageContainer className="relative py-16 md:py-24 lg:py-32">
        <nav className="mb-6 text-sm" aria-label="Breadcrumb">
          <ol className="flex items-center gap-2 text-white/70">
            <li>
              <Link to="/" className="transition-colors hover:text-white">Home</Link>
            </li>
            <li aria-hidden="true">/</li>
            <li>
              <Link to="/explore" className="transition-colors hover:text-white">Explore</Link>
            </li>
            <li aria-hidden="true">/</li>
            <li aria-current="page" className="text-white">{name}</li>
          </ol>
        </nav>

        <div className="max-w-3xl">
          <div className="mb-4 flex flex-wrap items-center gap-3">
            {travelType && <Badge variant="highlight">{travelType}</Badge>}
            {region && <Badge variant="accent">{region}</Badge>}
          </div>

          <h1
            id="dest-hero-heading"
            className="text-balance text-4xl font-bold leading-tight text-white sm:text-5xl lg:text-6xl"
          >
            {name}
          </h1>

          <p className="mt-2 text-lg text-white/80">
            {country}
          </p>

          <p className="mt-6 max-w-2xl text-base leading-relaxed text-white/85 md:text-lg">
            {description}
          </p>
        </div>
      </PageContainer>
    </section>
  );
}
