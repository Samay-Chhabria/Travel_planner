import apiClient from './apiClient';

export async function getWeatherForDestination(destinationId, days = 5) {
  const response = await apiClient.get(`/destinations/${destinationId}/weather`, {
    params: { days },
  });
  return response.data?.data?.weather ?? null;
}
