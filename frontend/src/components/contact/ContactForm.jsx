import { useState } from 'react';
import Input from '../common/Input';
import Button from '../common/Button';
import { validateContactForm, hasErrors } from '../../utils/validators';

const INITIAL_FORM = { name: '', email: '', message: '' };
const INITIAL_ERRORS = { name: '', email: '', message: '' };

export default function ContactForm() {
  const [form, setForm] = useState(INITIAL_FORM);
  const [errors, setErrors] = useState(INITIAL_ERRORS);
  const [submitted, setSubmitted] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
    if (errors[name]) {
      setErrors((prev) => ({ ...prev, [name]: '' }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = validateContactForm(form);
    setErrors(validationErrors);

    if (hasErrors(validationErrors)) return;

    setSubmitted(true);
  };

  if (submitted) {
    return (
      <div className="rounded-card border border-accent/20 bg-accent/5 p-8 text-center">
        <div className="mx-auto mb-4 flex h-16 w-16 items-center justify-center rounded-full bg-accent/10">
          <svg className="h-8 w-8 text-accent" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
            <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clipRule="evenodd" />
          </svg>
        </div>
        <h3 className="mb-2 text-lg font-semibold text-primary">
          Message Sent!
        </h3>
        <p className="mb-6 text-sm text-secondary">
          Thank you for reaching out. We will get back to you soon.
        </p>
        <Button
          variant="secondary"
          onClick={() => {
            setForm(INITIAL_FORM);
            setSubmitted(false);
          }}
        >
          Send Another Message
        </Button>
      </div>
    );
  }

  return (
    <form onSubmit={handleSubmit} noValidate className="space-y-5">
      <Input
        label="Name"
        name="name"
        placeholder="Your name"
        required
        value={form.name}
        onChange={handleChange}
        error={errors.name}
      />

      <Input
        label="Email"
        name="email"
        type="email"
        placeholder="you@example.com"
        required
        value={form.email}
        onChange={handleChange}
        error={errors.email}
      />

      <Input
        label="Message"
        name="message"
        as="textarea"
        placeholder="How can we help you?"
        required
        rows={5}
        value={form.message}
        onChange={handleChange}
        error={errors.message}
      />

      <Button type="submit" variant="primary" size="lg" className="w-full">
        Send Message
      </Button>
    </form>
  );
}
