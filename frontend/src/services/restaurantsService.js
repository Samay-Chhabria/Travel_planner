import apiClient from './apiClient';

export async function getRestaurantsForDestination(destinationId, options = {}) {
  const response = await apiClient.get(`/destinations/${destinationId}/restaurants`, {
    params: options,
  });
  return response.data?.data?.restaurants ?? [];
}
