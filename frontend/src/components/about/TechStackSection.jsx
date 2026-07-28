import SectionWrapper from '../layout/SectionWrapper';
import Badge from '../common/Badge';

const TECH_CATEGORIES = [
  {
    category: 'Frontend',
    items: ['React', 'Vite', 'Tailwind CSS', 'React Router', 'Axios'],
  },
  {
    category: 'Backend',
    items: ['FastAPI', 'Pydantic', 'Uvicorn'],
  },
  {
    category: 'External APIs',
    items: ['Open-Meteo', 'Nominatim', 'OpenTripMap', 'REST Countries', 'Leaflet + OpenStreetMap'],
  },
  {
    category: 'Deployment',
    items: ['Vercel', 'Render'],
  },
];

export default function TechStackSection() {
  return (
    <SectionWrapper id="tech" background="surface" ariaLabelledby="tech-heading">
      <div className="text-center mb-12">
        <h2
          id="tech-heading"
          className="text-3xl font-bold text-primary sm:text-4xl"
        >
          Technologies Used
        </h2>
        <p className="mt-4 max-w-2xl mx-auto text-secondary">
          Built with modern tools and free travel APIs
        </p>
      </div>

      <div className="mx-auto grid max-w-4xl gap-8 sm:grid-cols-2">
        {TECH_CATEGORIES.map((cat) => (
          <div key={cat.category}>
            <h3 className="mb-4 text-sm font-semibold uppercase tracking-wide text-accent">
              {cat.category}
            </h3>
            <div className="flex flex-wrap gap-2">
              {cat.items.map((tech) => (
                <Badge key={tech} variant="default">
                  {tech}
                </Badge>
              ))}
            </div>
          </div>
        ))}
      </div>
    </SectionWrapper>
  );
}
