import axios from 'axios';
import { API_BASE_URL } from '../utils/constants';

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 15000,
});

apiClient.interceptors.request.use(
  (config) => config,
  (error) => Promise.reject(error),
);

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      const serverMessage =
        error.response.data?.error?.message ||
        error.response.data?.message;
      const message =
        serverMessage ||
        `Request failed with status ${error.response.status}`;
      return Promise.reject(new Error(message));
    }

    if (error.code === 'ECONNABORTED') {
      return Promise.reject(new Error('Request timed out. Please try again.'));
    }

    if (!navigator.onLine) {
      return Promise.reject(new Error('No internet connection. Please check your network.'));
    }

    return Promise.reject(
      new Error(error.message || 'Something went wrong. Please try again.'),
    );
  },
);

export default apiClient;
