import apiClient from './apiClient';

export async function generateTripPlan(planRequest) {
  const response = await apiClient.post('/trip-planner/generate', planRequest);
  return response.data?.data?.plan ?? null;
}
