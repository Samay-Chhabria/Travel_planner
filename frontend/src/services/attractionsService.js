import apiClient from './apiClient';

export async function getAttractionsForDestination(destinationId, options = {}) {
  const response = await apiClient.get(`/destinations/${destinationId}/attractions`, {
    params: options,
  });
  return response.data?.data?.attractions ?? [];
}
