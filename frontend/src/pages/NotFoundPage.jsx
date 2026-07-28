import { Link } from 'react-router-dom';
import PageContainer from '../components/layout/PageContainer';

export default function NotFoundPage() {
  return (
    <div className="bg-background">
      <PageContainer className="flex flex-col items-center justify-center py-24 text-center">
        <div className="mb-6 flex h-24 w-24 items-center justify-center rounded-full bg-highlight/10">
          <span className="text-5xl font-bold text-highlight">404</span>
        </div>
        <h1 className="mb-2 text-3xl font-bold text-primary">Page not found</h1>
        <p className="mb-8 max-w-md text-secondary">
          The page you&apos;re looking for doesn&apos;t exist or may have been moved.
        </p>
        <div className="flex flex-col gap-3 sm:flex-row">
          <Link
            to="/"
            className="inline-flex min-h-[44px] items-center justify-center gap-2 rounded-pill bg-accent px-6 py-3 font-medium text-white shadow-sm transition-all duration-200 hover:bg-accent/90 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2"
          >
            Go Home
          </Link>
          <Link
            to="/explore"
            className="inline-flex min-h-[44px] items-center justify-center gap-2 rounded-pill border border-border bg-surface px-6 py-3 font-medium text-primary shadow-sm transition-all duration-200 hover:bg-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent/40 focus-visible:ring-offset-2"
          >
            Explore Destinations
          </Link>
        </div>
      </PageContainer>
    </div>
  );
}
