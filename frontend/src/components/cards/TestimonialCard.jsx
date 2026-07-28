export default function TestimonialCard({ testimonial }) {
  const { quote, name, role, location, avatarUrl } = testimonial;

  return (
    <figure className="flex h-full flex-col rounded-card border border-border bg-surface p-6 shadow-card md:p-8">
      <blockquote className="flex-1">
        <svg
          className="mb-4 h-8 w-8 text-highlight/40"
          fill="currentColor"
          viewBox="0 0 24 24"
          aria-hidden="true"
        >
          <path d="M4.583 17.321C3.553 16.227 3 15 3 13.011c0-3.5 2.457-6.637 6.03-8.188l.893 1.378c-3.335 1.804-3.987 4.145-4.247 5.621.537-.278 1.24-.375 1.929-.311 1.804.167 3.226 1.648 3.226 3.489a3.016 3.016 0 01-3.016 3.016c-1.118 0-2.017-.668-2.445-1.626zm9.75 0C13.303 16.227 12.75 15 12.75 13.011c0-3.5 2.457-6.637 6.03-8.188l.893 1.378c-3.335 1.804-3.987 4.145-4.247 5.621.537-.278 1.24-.375 1.929-.311 1.804.167 3.226 1.648 3.226 3.489a3.016 3.016 0 01-3.016 3.016c-1.118 0-2.017-.668-2.445-1.626z" />
        </svg>
        <p className="text-base leading-relaxed text-primary md:text-lg">&ldquo;{quote}&rdquo;</p>
      </blockquote>
      <figcaption className="mt-6 flex items-center gap-4 border-t border-border pt-6">
        <img
          src={avatarUrl}
          alt={`Photo of ${name}`}
          className="h-12 w-12 rounded-full object-cover"
          loading="lazy"
        />
        <div>
          <p className="font-semibold text-primary">{name}</p>
          <p className="text-sm text-secondary">
            {role} · {location}
          </p>
        </div>
      </figcaption>
    </figure>
  );
}
