import apiClient from './apiClient';

export async function getFeaturedDestinations(limit = 6) {
  const response = await apiClient.get('/destinations/featured', {
    params: { limit },
  });
  return response.data?.data?.destinations ?? [];
}

export async function searchDestinations(query, options = {}) {
  const response = await apiClient.get('/destinations/search', {
    params: { q: query, ...options },
  });
  return response.data?.data?.results ?? [];
}

export async function getDestinationById(destinationId) {
  const response = await apiClient.get(`/destinations/${destinationId}`);
  return response.data?.data?.destination ?? null;
}
