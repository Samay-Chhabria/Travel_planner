import PageContainer from '../components/layout/PageContainer';
import ContactForm from '../components/contact/ContactForm';
import ContactInfo from '../components/contact/ContactInfo';
import FAQSection from '../components/contact/FAQSection';

export default function ContactPage() {
  return (
    <div className="bg-background">
      {/* Hero */}
      <div className="pt-16 pb-12 md:pt-24 md:pb-16">
        <PageContainer>
          <div className="max-w-2xl">
            <p className="mb-4 text-sm font-semibold uppercase tracking-widest text-accent">
              Contact
            </p>
            <h1 className="text-3xl font-bold text-primary md:text-4xl">
              Get in Touch
            </h1>
            <p className="mt-4 text-lg text-secondary">
              Have a question, suggestion, or just want to say hello?
              We would love to hear from you.
            </p>
          </div>
        </PageContainer>
      </div>

      {/* Form + Info */}
      <section className="pb-16 md:pb-24">
        <PageContainer>
          <div className="grid gap-12 lg:grid-cols-[1fr_380px]">
            <div className="rounded-card border border-border bg-surface p-6 sm:p-8 shadow-card">
              <h2 className="mb-6 text-xl font-semibold text-primary">
                Send us a message
              </h2>
              <ContactForm />
            </div>

            <div>
              <ContactInfo />
            </div>
          </div>
        </PageContainer>
      </section>

      {/* FAQ */}
      <section className="border-t border-border bg-surface py-16 md:py-24">
        <PageContainer>
          <FAQSection />
        </PageContainer>
      </section>
    </div>
  );
}
