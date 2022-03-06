import axios from "axios";

const authService = axios.create({
  baseURL: process.env.VUE_APP_AUTH_URL,
});

const apiService = axios.create({
  baseURL: process.env.VUE_APP_URL,
});
export { authService, apiService };
