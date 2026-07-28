import SectionWrapper from '../layout/SectionWrapper';
import TestimonialCard from '../cards/TestimonialCard';
import { TESTIMONIALS } from '../../utils/constants';

export default function TestimonialsSection() {
  return (
    <SectionWrapper background="default" ariaLabelledby="testimonials-heading">
      <div className="mx-auto mb-10 max-w-2xl text-center md:mb-12">
        <p className="mb-2 text-sm font-medium uppercase tracking-widest text-accent">
          Trusted by travelers
        </p>
        <h2
          id="testimonials-heading"
          className="text-3xl font-bold text-primary md:text-4xl"
        >
          What travelers are saying
        </h2>
        <p className="mt-3 text-secondary md:text-lg">
          Real stories from people who use Travel Planner to discover destinations
          and plan with ease.
        </p>
      </div>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {TESTIMONIALS.map((testimonial) => (
          <TestimonialCard key={testimonial.id} testimonial={testimonial} />
        ))}
      </div>
    </SectionWrapper>
  );
}
