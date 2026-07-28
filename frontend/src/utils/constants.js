export const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api/v1';

export const NAV_LINKS = [
  { label: 'Home', path: '/' },
  { label: 'Explore', path: '/explore' },
  { label: 'Planner', path: '/planner' },
  { label: 'About', path: '/about' },
  { label: 'Contact', path: '/contact' },
];

export const POPULAR_THEMES = [
  {
    id: 'beach',
    title: 'Beach Escapes',
    description: 'Sun, sand, and serene coastal getaways',
    imageUrl:
      'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800&q=80',
    tag: 'Relaxation',
  },
  {
    id: 'culture',
    title: 'Culture & History',
    description: 'Museums, landmarks, and timeless city stories',
    imageUrl:
      'https://images.unsplash.com/photo-1548013146-72479768bada?w=800&q=80',
    tag: 'Heritage',
  },
  {
    id: 'adventure',
    title: 'Adventure',
    description: 'Trails, peaks, and outdoor thrills',
    imageUrl:
      'https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800&q=80',
    tag: 'Outdoors',
  },
  {
    id: 'city',
    title: 'City Breaks',
    description: 'Vibrant neighborhoods, food, and nightlife',
    imageUrl:
      'https://images.unsplash.com/photo-1480714378408-67cf0d13bc1b?w=800&q=80',
    tag: 'Urban',
  },
  {
    id: 'nature',
    title: 'Nature Retreats',
    description: 'Forests, lakes, and peaceful landscapes',
    imageUrl:
      'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&q=80',
    tag: 'Scenic',
  },
  {
    id: 'food',
    title: 'Food & Wine',
    description: 'Culinary journeys and local flavors',
    imageUrl:
      'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=800&q=80',
    tag: 'Gastronomy',
  },
];

export const TESTIMONIALS = [
  {
    id: '1',
    quote:
      'Travel Planner helped us discover hidden gems in Kyoto we never would have found on our own. The layout is calm and easy to follow.',
    name: 'Sarah Mitchell',
    role: 'Travel enthusiast',
    location: 'Portland, OR',
    avatarUrl:
      'https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=150&q=80',
  },
  {
    id: '2',
    quote:
      'I love how spacious and intuitive the experience feels. Planning our Barcelona trip took minutes instead of hours.',
    name: 'James Chen',
    role: 'Weekend explorer',
    location: 'San Francisco, CA',
    avatarUrl:
      'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&q=80',
  },
  {
    id: '3',
    quote:
      'The featured destinations and travel themes gave us instant inspiration. It feels premium without being overwhelming.',
    name: 'Elena Rodriguez',
    role: 'Family traveler',
    location: 'Austin, TX',
    avatarUrl:
      'https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&q=80',
  },
];

export const ALL_DESTINATIONS = [
  {
    id: 'paris-france',
    name: 'Paris',
    country: 'France',
    region: 'Europe',
    slug: 'paris-france',
    description: 'The City of Light — art, cuisine, and romance along the Seine.',
    image_url:
      'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=800&q=80',
    highlights: ['Art', 'Food', 'Romance'],
    best_time_to_visit: 'April to June',
    travel_type: 'City',
  },
  {
    id: 'tokyo-japan',
    name: 'Tokyo',
    country: 'Japan',
    region: 'Asia',
    slug: 'tokyo-japan',
    description: 'A dazzling blend of tradition, technology, and incredible food.',
    image_url:
      'https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?w=800&q=80',
    highlights: ['Culture', 'Food', 'Nightlife'],
    best_time_to_visit: 'March to May',
    travel_type: 'City',
  },
  {
    id: 'bali-indonesia',
    name: 'Bali',
    country: 'Indonesia',
    region: 'Asia',
    slug: 'bali-indonesia',
    description: 'Lush rice terraces, temples, and tranquil beach retreats.',
    image_url:
      'https://images.unsplash.com/photo-1537996194471-e657df975ab4?w=800&q=80',
    highlights: ['Beach', 'Wellness', 'Nature'],
    best_time_to_visit: 'April to October',
    travel_type: 'Beach',
  },
  {
    id: 'santorini-greece',
    name: 'Santorini',
    country: 'Greece',
    region: 'Europe',
    slug: 'santorini-greece',
    description: 'Iconic whitewashed villages overlooking the Aegean Sea.',
    image_url:
      'https://images.unsplash.com/photo-1613395877344-13d4a8e0d49e?w=800&q=80',
    highlights: ['Scenic', 'Romance', 'Food'],
    best_time_to_visit: 'May to September',
    travel_type: 'Beach',
  },
  {
    id: 'new-york-usa',
    name: 'New York',
    country: 'United States',
    region: 'North America',
    slug: 'new-york-usa',
    description: 'The city that never sleeps — culture, dining, and iconic sights.',
    image_url:
      'https://images.unsplash.com/photo-1534430480872-3498386e7856?w=800&q=80',
    highlights: ['Culture', 'Shopping', 'Food'],
    best_time_to_visit: 'April to June',
    travel_type: 'City',
  },
  {
    id: 'cape-town-south-africa',
    name: 'Cape Town',
    country: 'South Africa',
    region: 'Africa',
    slug: 'cape-town-south-africa',
    description: 'Stunning coastlines, Table Mountain, and vibrant neighborhoods.',
    image_url:
      'https://images.unsplash.com/photo-1516026672322-bc52d61a55d5?w=800&q=80',
    highlights: ['Nature', 'Adventure', 'Scenic'],
    best_time_to_visit: 'November to March',
    travel_type: 'Adventure',
  },
  {
    id: 'london-united-kingdom',
    name: 'London',
    country: 'United Kingdom',
    region: 'Europe',
    slug: 'london-united-kingdom',
    description:
      'Historic capital of England — royal palaces, world-class museums, and a vibrant cultural scene along the Thames.',
    image_url:
      'https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?w=800&q=80',
    highlights: ['History', 'Culture', 'Theatre'],
    best_time_to_visit: 'March to September',
    travel_type: 'City',
  },
  {
    id: 'karachi-pakistan',
    name: 'Karachi',
    country: 'Pakistan',
    region: 'Asia',
    slug: 'karachi-pakistan',
    description:
      "Pakistan's bustling coastal metropolis — colonial architecture, vibrant bazaars, and the Arabian Sea coastline.",
    image_url:
      'https://images.unsplash.com/photo-1570168007204-dfb528c6958f?w=800&q=80',
    highlights: ['Culture', 'Food', 'Beaches'],
    best_time_to_visit: 'November to February',
    travel_type: 'City',
  },
  {
    id: 'rome-italy',
    name: 'Rome',
    country: 'Italy',
    region: 'Europe',
    slug: 'rome-italy',
    description: 'The Eternal City — ancient ruins, art, and la dolce vita.',
    image_url:
      'https://images.unsplash.com/photo-1552832230-c0197dd311b5?w=800&q=80',
    highlights: ['History', 'Art', 'Food'],
    best_time_to_visit: 'April to June',
    travel_type: 'Culture',
  },
  {
    id: 'barcelona-spain',
    name: 'Barcelona',
    country: 'Spain',
    region: 'Europe',
    slug: 'barcelona-spain',
    description: 'Gaudí masterpieces, vibrant streets, and Mediterranean charm.',
    image_url:
      'https://images.unsplash.com/photo-1583422409516-2895a77efded?w=800&q=80',
    highlights: ['Architecture', 'Beach', 'Nightlife'],
    best_time_to_visit: 'May to June',
    travel_type: 'City',
  },
  {
    id: 'maldives',
    name: 'Maldives',
    country: 'Maldives',
    region: 'Asia',
    slug: 'maldives',
    description: 'Crystal-clear waters, overwater villas, and pristine beaches.',
    image_url:
      'https://images.unsplash.com/photo-1514282401047-d79a71a590e8?w=800&q=80',
    highlights: ['Beach', 'Luxury', 'Snorkeling'],
    best_time_to_visit: 'November to April',
    travel_type: 'Beach',
  },
  {
    id: 'kyoto-japan',
    name: 'Kyoto',
    country: 'Japan',
    region: 'Asia',
    slug: 'kyoto-japan',
    description: 'Ancient temples, traditional gardens, and geisha culture.',
    image_url:
      'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=800&q=80',
    highlights: ['Culture', 'Temples', 'Nature'],
    best_time_to_visit: 'March to May',
    travel_type: 'Culture',
  },
  {
    id: 'machu-picchu-peru',
    name: 'Machu Picchu',
    country: 'Peru',
    region: 'South America',
    slug: 'machu-picchu-peru',
    description: 'The legendary Incan citadel set high in the Andes Mountains.',
    image_url:
      'https://images.unsplash.com/photo-1526392060635-9d6019884377?w=800&q=80',
    highlights: ['History', 'Hiking', 'Scenic'],
    best_time_to_visit: 'May to September',
    travel_type: 'Adventure',
  },
  {
    id: 'swiss-alps',
    name: 'Swiss Alps',
    country: 'Switzerland',
    region: 'Europe',
    slug: 'swiss-alps',
    description: 'Majestic peaks, pristine lakes, and world-class skiing.',
    image_url:
      'https://images.unsplash.com/photo-1531366936337-7c912a4589a7?w=800&q=80',
    highlights: ['Skiing', 'Hiking', 'Scenic'],
    best_time_to_visit: 'December to March',
    travel_type: 'Adventure',
  },
  {
    id: 'dubai-uae',
    name: 'Dubai',
    country: 'United Arab Emirates',
    region: 'Asia',
    slug: 'dubai-uae',
    description: 'Futuristic skyline, luxury shopping, and desert adventures.',
    image_url:
      'https://images.unsplash.com/photo-1512453979798-5ea266f8880c?w=800&q=80',
    highlights: ['Luxury', 'Shopping', 'Architecture'],
    best_time_to_visit: 'November to March',
    travel_type: 'City',
  },
  {
    id: 'queenstown-new-zealand',
    name: 'Queenstown',
    country: 'New Zealand',
    region: 'Oceania',
    slug: 'queenstown-new-zealand',
    description: 'Adventure capital surrounded by stunning mountains and lakes.',
    image_url:
      'https://images.unsplash.com/photo-1507699622108-4be3abd695ad?w=800&q=80',
    highlights: ['Adventure', 'Nature', 'Scenic'],
    best_time_to_visit: 'June to September',
    travel_type: 'Adventure',
  },
  {
    id: 'marrakech-morocco',
    name: 'Marrakech',
    country: 'Morocco',
    region: 'Africa',
    slug: 'marrakech-morocco',
    description: 'Vibrant souks, stunning palaces, and enchanting riads.',
    image_url:
      'https://images.unsplash.com/photo-1597212618440-806262de4f6b?w=800&q=80',
    highlights: ['Culture', 'Markets', 'Architecture'],
    best_time_to_visit: 'March to May',
    travel_type: 'Culture',
  },
  {
    id: 'banff-canada',
    name: 'Banff',
    country: 'Canada',
    region: 'North America',
    slug: 'banff-canada',
    description: 'Turquoise lakes, towering peaks, and pristine wilderness.',
    image_url:
      'https://images.unsplash.com/photo-1503614472-8c93d56e92ce?w=800&q=80',
    highlights: ['Nature', 'Hiking', 'Skiing'],
    best_time_to_visit: 'June to August',
    travel_type: 'Nature',
  },
  {
    id: 'santorini-greece-alt',
    name: 'Mykonos',
    country: 'Greece',
    region: 'Europe',
    slug: 'mykonos-greece',
    description: 'White-washed buildings, beautiful beaches, and legendary nightlife.',
    image_url:
      'https://images.unsplash.com/photo-1601581875039-e899893d520c?w=800&q=80',
    highlights: ['Beach', 'Nightlife', 'Scenic'],
    best_time_to_visit: 'May to September',
    travel_type: 'Beach',
  },
  {
    id: 'patagonia-argentina',
    name: 'Patagonia',
    country: 'Argentina',
    region: 'South America',
    slug: 'patagonia-argentina',
    description: 'Vast wilderness, glaciers, and dramatic mountain landscapes.',
    image_url:
      'https://images.unsplash.com/photo-1531761535209-180857e963b9?w=800&q=80',
    highlights: ['Hiking', 'Nature', 'Glaciers'],
    best_time_to_visit: 'October to March',
    travel_type: 'Adventure',
  },
  {
    id: 'petra-jordan',
    name: 'Petra',
    country: 'Jordan',
    region: 'Asia',
    slug: 'petra-jordan',
    description: 'The ancient rose-red city carved into stunning desert cliffs.',
    image_url:
      'https://images.unsplash.com/photo-1555952517-2e8e729e0b44?w=800&q=80',
    highlights: ['History', 'Adventure', 'Culture'],
    best_time_to_visit: 'March to May',
    travel_type: 'Culture',
  },
  {
    id: 'hawaii-usa',
    name: 'Hawaii',
    country: 'United States',
    region: 'North America',
    slug: 'hawaii-usa',
    description: 'Tropical paradise with volcanoes, beaches, and aloha spirit.',
    image_url:
      'https://images.unsplash.com/photo-1507876466758-bc54f384809c?w=800&q=80',
    highlights: ['Beach', 'Nature', 'Surfing'],
    best_time_to_visit: 'April to October',
    travel_type: 'Beach',
  },
];

export const FALLBACK_FEATURED_DESTINATIONS = ALL_DESTINATIONS.slice(0, 6);

export const PRICE_LEVEL_MAP = {
  budget: { label: 'Budget', display: '$' },
  mid_range: { label: 'Mid-range', display: '$$' },
  luxury: { label: 'Luxury', display: '$$$' },
};

export function formatPriceLevel(level) {
  return PRICE_LEVEL_MAP[level] || { label: level || 'Unknown', display: '$$' };
}
