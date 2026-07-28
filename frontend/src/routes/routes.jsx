import { lazy, Suspense } from 'react';
import { Routes, Route } from 'react-router-dom';
import MainLayout from '../layouts/MainLayout';

const HomePage = lazy(() => import('../pages/HomePage'));
const ExplorePage = lazy(() => import('../pages/ExplorePage'));
const DestinationDetailsPage = lazy(() => import('../pages/DestinationDetailsPage'));
const TripPlannerPage = lazy(() => import('../pages/TripPlannerPage'));
const AboutPage = lazy(() => import('../pages/AboutPage'));
const ContactPage = lazy(() => import('../pages/ContactPage'));
const NotFoundPage = lazy(() => import('../pages/NotFoundPage'));

function PageLoader() {
  return (
    <div className="flex min-h-[50vh] items-center justify-center">
      <div className="h-8 w-8 animate-spin rounded-full border-4 border-accent border-t-transparent" />
    </div>
  );
}

export default function AppRoutes() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route index element={<Suspense fallback={<PageLoader />}><HomePage /></Suspense>} />
        <Route path="explore" element={<Suspense fallback={<PageLoader />}><ExplorePage /></Suspense>} />
        <Route path="destinations/:slug" element={<Suspense fallback={<PageLoader />}><DestinationDetailsPage /></Suspense>} />
        <Route path="planner" element={<Suspense fallback={<PageLoader />}><TripPlannerPage /></Suspense>} />
        <Route path="about" element={<Suspense fallback={<PageLoader />}><AboutPage /></Suspense>} />
        <Route path="contact" element={<Suspense fallback={<PageLoader />}><ContactPage /></Suspense>} />
        <Route path="*" element={<Suspense fallback={<PageLoader />}><NotFoundPage /></Suspense>} />
      </Route>
    </Routes>
  );
}
