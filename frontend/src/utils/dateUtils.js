export function daysBetween(start, end) {
  if (!start || !end) return 0;
  return Math.ceil((new Date(end) - new Date(start)) / (1000 * 60 * 60 * 24)) + 1;
}

export function formatDateRange(start, end) {
  if (!start || !end) return 'Not selected';
  const opts = { month: 'short', day: 'numeric' };
  const startStr = new Date(start).toLocaleDateString('en-US', opts);
  const endStr = new Date(end).toLocaleDateString('en-US', { ...opts, year: 'numeric' });
  return `${startStr} — ${endStr}`;
}
