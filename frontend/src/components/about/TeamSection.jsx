import SectionWrapper from '../layout/SectionWrapper';
import Button from '../common/Button';

export default function TeamSection() {
  return (
    <SectionWrapper id="team" background="default" ariaLabelledby="team-heading">
      <div className="mx-auto max-w-2xl text-center">
        <h2
          id="team-heading"
          className="text-3xl font-bold text-primary sm:text-4xl"
        >
          Built With Passion
        </h2>
        <p className="mt-4 text-secondary">
          A project crafted with care for modern travelers
        </p>
      </div>

      <div className="mx-auto mt-12 max-w-md">
        <div className="rounded-card border border-border bg-surface p-8 shadow-card text-center">
          <div className="mx-auto mb-4 flex h-20 w-20 items-center justify-center rounded-full bg-accent/10">
            <svg
              className="h-10 w-10 text-accent"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              aria-hidden="true"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={1.5}
                d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"
              />
            </svg>
          </div>

          <h3 className="text-lg font-semibold text-primary">
            Travel Planner
          </h3>
          <p className="mt-1 text-sm text-secondary">
            Frontend Engineer
          </p>

          <p className="mt-4 text-sm leading-relaxed text-secondary">
            Building beautiful, functional travel experiences with modern web technologies.
          </p>

          <div className="mt-6 flex justify-center gap-3">
            <Button variant="primary" to="/planner">
              Plan a Trip
            </Button>
            <Button variant="secondary" to="/contact">
              Get in Touch
            </Button>
          </div>
        </div>
      </div>
    </SectionWrapper>
  );
}
