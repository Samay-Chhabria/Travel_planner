import { useState } from 'react';

const FAQ_ITEMS = [
  {
    question: 'What is Travel Planner?',
    answer:
      'Travel Planner is a modern web platform that helps you discover amazing destinations and create personalized trip itineraries. It aggregates free travel APIs to provide destination info, weather data, attractions, and more.',
  },
  {
    question: 'Is it free to use?',
    answer:
      'Yes! Travel Planner is completely free to use. There are no hidden fees, subscriptions, or premium tiers. It was built as a portfolio project to demonstrate modern web development skills.',
  },
  {
    question: 'How does trip planning work?',
    answer:
      'Simply choose your destination, set your travel dates, pick your budget level, select the number of travelers, and choose a travel theme. The planner then generates a personalized itinerary based on your preferences.',
  },
  {
    question: 'Can I save my trips?',
    answer:
      'Trip saving is planned for a future phase that will include user accounts and persistent storage. For now, you can plan trips and view the generated itinerary during your session.',
  },
  {
    question: 'How do I report a bug or suggest a feature?',
    answer:
      'You can reach us through the contact form on this page, or open an issue on our GitHub repository. We welcome feedback and contributions to make Travel Planner even better.',
  },
];

function FAQItem({ item, isOpen, onToggle, id }) {
  const panelId = `faq-panel-${id}`;
  const buttonId = `faq-button-${id}`;

  return (
    <div className="border-b border-border last:border-b-0">
      <button
        type="button"
        id={buttonId}
        onClick={onToggle}
        className="flex w-full items-center justify-between gap-4 py-5 text-left"
        aria-expanded={isOpen}
        aria-controls={panelId}
      >
        <span className="text-base font-medium text-primary">
          {item.question}
        </span>
        <svg
          className={[
            'h-5 w-5 shrink-0 text-secondary transition-transform duration-200',
            isOpen && 'rotate-180',
          ].join(' ')}
          fill="none"
          viewBox="0 0 24 24"
          stroke="currentColor"
          aria-hidden="true"
        >
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 9l-7 7-7-7" />
        </svg>
      </button>

      <div
        id={panelId}
        role="region"
        aria-labelledby={buttonId}
        className={[
          'overflow-hidden transition-all duration-200',
          isOpen ? 'max-h-40 pb-5' : 'max-h-0',
        ].join(' ')}
      >
        <p className="text-sm leading-relaxed text-secondary">
          {item.answer}
        </p>
      </div>
    </div>
  );
}

export default function FAQSection() {
  const [openIndex, setOpenIndex] = useState(null);

  return (
    <div>
      <h2 className="mb-2 text-2xl font-bold text-primary sm:text-3xl">
        Frequently Asked Questions
      </h2>
      <p className="mb-8 text-secondary">
        Quick answers to common questions
      </p>

      <div className="rounded-card border border-border bg-surface px-6 shadow-card">
        {FAQ_ITEMS.map((item, index) => (
          <FAQItem
            key={item.question}
            id={index}
            item={item}
            isOpen={openIndex === index}
            onToggle={() => setOpenIndex(openIndex === index ? null : index)}
          />
        ))}
      </div>
    </div>
  );
}
