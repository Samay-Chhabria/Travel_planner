import HeroSection from '../components/sections/HeroSection';
import FeaturedDestinations from '../components/sections/FeaturedDestinations';
import PopularThemes from '../components/sections/PopularThemes';
import TestimonialsSection from '../components/sections/TestimonialsSection';

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <FeaturedDestinations />
      <PopularThemes />
      <TestimonialsSection />
    </>
  );
}
