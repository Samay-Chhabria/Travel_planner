export function validateContactForm(form) {
  const errors = { name: '', email: '', message: '' };

  if (!form.name.trim()) {
    errors.name = 'Name is required';
  }

  if (!form.email.trim()) {
    errors.email = 'Email is required';
  } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
    errors.email = 'Please enter a valid email';
  }

  if (!form.message.trim()) {
    errors.message = 'Message is required';
  } else if (form.message.trim().length < 10) {
    errors.message = 'Message must be at least 10 characters';
  }

  return errors;
}

export function hasErrors(errors) {
  return Object.values(errors).some(Boolean);
}
