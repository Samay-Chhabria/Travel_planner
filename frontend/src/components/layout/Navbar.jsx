import { Link, useLocation } from 'react-router-dom';
import { useState } from 'react';
import { NAV_LINKS } from '../../utils/constants';
import Button from '../common/Button';
import PageContainer from './PageContainer';

function NavLink({ to, label, onClick }) {
  const { pathname } = useLocation();
  const isActive = pathname === to;

  return (
    <Link
      to={to}
      onClick={onClick}
      className={[
        'rounded-lg px-3 py-2 text-sm font-medium transition-colors duration-200',
        isActive
          ? 'text-accent'
          : 'text-secondary hover:text-primary focus-visible:text-primary',
      ].join(' ')}
      aria-current={isActive ? 'page' : undefined}
    >
      {label}
    </Link>
  );
}

export default function Navbar() {
  const [menuOpen, setMenuOpen] = useState(false);

  const closeMenu = () => setMenuOpen(false);

  return (
    <header className="sticky top-0 z-50 border-b border-border/60 bg-surface/95 shadow-nav backdrop-blur-sm">
      <a
        href="#main-content"
        className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-[100] focus:rounded-card focus:bg-accent focus:px-4 focus:py-2 focus:text-white focus:outline-none"
      >
        Skip to content
      </a>
      <PageContainer>
        <nav
          className="flex h-16 items-center justify-between md:h-20"
          aria-label="Main navigation"
        >
          <Link
            to="/"
            className="flex items-center gap-2 text-lg font-bold tracking-tight text-primary transition-colors hover:text-accent md:text-xl"
          >
            <span
              className="flex h-9 w-9 items-center justify-center rounded-full bg-accent text-sm text-white"
              aria-hidden="true"
            >
              TP
            </span>
            <span>Travel Planner</span>
          </Link>

          <ul className="hidden items-center gap-1 md:flex" role="list">
            {NAV_LINKS.map(({ label, path }) => (
              <li key={path}>
                <NavLink to={path} label={label} />
              </li>
            ))}
          </ul>

          <div className="hidden md:block">
            <Button variant="highlight" size="sm" to="/planner">
              Plan a Trip
            </Button>
          </div>

          <button
            type="button"
            className="inline-flex h-11 w-11 items-center justify-center rounded-lg text-primary hover:bg-background md:hidden"
            aria-expanded={menuOpen}
            aria-controls="mobile-menu"
            aria-label={menuOpen ? 'Close menu' : 'Open menu'}
            onClick={() => setMenuOpen((open) => !open)}
          >
            {menuOpen ? (
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            ) : (
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden="true">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            )}
          </button>
        </nav>
      </PageContainer>

      {menuOpen && (
        <div
          id="mobile-menu"
          className="border-t border-border bg-surface px-4 py-4 md:hidden"
        >
          <ul className="flex flex-col gap-1" role="list">
            {NAV_LINKS.map(({ label, path }) => (
              <li key={path}>
                <NavLink to={path} label={label} onClick={closeMenu} />
              </li>
            ))}
          </ul>
          <div className="mt-4">
            <Button
              variant="highlight"
              size="md"
              to="/planner"
              className="w-full"
              onClick={closeMenu}
            >
              Plan a Trip
            </Button>
          </div>
        </div>
      )}
    </header>
  );
}
