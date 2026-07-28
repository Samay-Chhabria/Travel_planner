import Button from '../common/Button';
import PageContainer from '../layout/PageContainer';

export default function PlanTripCTA({ destination }) {
  const { name } = destination;

  return (
    <section className="bg-accent py-16 md:py-20" aria-labelledby="cta-heading">
      <PageContainer>
        <div className="mx-auto max-w-2xl text-center">
          <h2
            id="cta-heading"
            className="text-balance text-3xl font-bold text-white md:text-4xl"
          >
            Ready to explore {name}?
          </h2>
          <p className="mt-4 text-base text-white/85 md:text-lg">
            Let us help you create the perfect trip itinerary. Start planning your adventure today.
          </p>
          <div className="mt-8 flex flex-col items-center justify-center gap-4 sm:flex-row">
            <Button
              variant="highlight"
              size="lg"
              to="/planner"
            >
              Plan Your Trip
            </Button>
            <Button
              variant="ghost"
              size="lg"
              to="/explore"
              className="border-white/30 text-white hover:bg-white/10"
            >
              Explore More
            </Button>
          </div>
        </div>
      </PageContainer>
    </section>
  );
}
