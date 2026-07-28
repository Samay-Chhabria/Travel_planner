import apiClient from './apiClient';

export async function getHotelsForDestination(destinationId, options = {}) {
  const response = await apiClient.get(`/destinations/${destinationId}/hotels`, {
    params: options,
  });
  return response.data?.data?.hotels ?? [];
}
