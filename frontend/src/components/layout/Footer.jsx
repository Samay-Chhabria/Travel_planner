import { Link } from 'react-router-dom';
import { NAV_LINKS } from '../../utils/constants';
import PageContainer from './PageContainer';

const FOOTER_LINKS = {
  explore: [
    { label: 'Destinations', path: '/explore' },
    { label: 'Trip Planner', path: '/planner' },
    { label: 'Popular Themes', path: '/#themes' },
  ],
  company: [
    { label: 'About', path: '/about' },
    { label: 'Contact', path: '/contact' },
  ],
};

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="border-t border-border bg-surface" aria-label="Site footer">
      <PageContainer className="py-12 md:py-16">
        <div className="grid gap-10 md:grid-cols-2 lg:grid-cols-4">
          <div className="lg:col-span-2">
            <Link
              to="/"
              className="inline-flex items-center gap-2 text-lg font-bold text-primary"
            >
              <span
                className="flex h-9 w-9 items-center justify-center rounded-full bg-accent text-sm text-white"
                aria-hidden="true"
              >
                TP
              </span>
              Travel Planner
            </Link>
            <p className="mt-4 max-w-md text-secondary">
              Discover destinations, explore travel themes, and plan smarter
              trips with a calm, inspiring experience built for modern travelers.
            </p>
          </div>

          <div>
            <h2 className="text-sm font-semibold uppercase tracking-wide text-primary">
              Explore
            </h2>
            <ul className="mt-4 space-y-3" role="list">
              {FOOTER_LINKS.explore.map(({ label, path }) => (
                <li key={path}>
                  <Link
                    to={path}
                    className="text-secondary transition-colors hover:text-accent"
                  >
                    {label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div>
            <h2 className="text-sm font-semibold uppercase tracking-wide text-primary">
              Company
            </h2>
            <ul className="mt-4 space-y-3" role="list">
              {FOOTER_LINKS.company.map(({ label, path }) => (
                <li key={path}>
                  <Link
                    to={path}
                    className="text-secondary transition-colors hover:text-accent"
                  >
                    {label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="mt-12 flex flex-col items-center justify-between gap-4 border-t border-border pt-8 sm:flex-row">
          <p className="text-sm text-secondary">
            &copy; {currentYear} Travel Planner. All rights reserved.
          </p>
          <nav aria-label="Footer navigation">
            <ul className="flex flex-wrap justify-center gap-4 sm:gap-6" role="list">
              {NAV_LINKS.map(({ label, path }) => (
                <li key={path}>
                  <Link
                    to={path}
                    className="text-sm text-secondary transition-colors hover:text-accent"
                  >
                    {label}
                  </Link>
                </li>
              ))}
            </ul>
          </nav>
        </div>
      </PageContainer>
    </footer>
  );
}
