import { apiService } from "@/api";
import authHeader from "@/services/auth-header";
export const CategoriesAPI = {
  getCategoryCollection: async () => {
    const res = (await apiService.get("/category/", { headers: authHeader() }))
      .data;
    return res;
  },
  createCategory: async (data) => {
    const res = (
      await apiService.post("/category/", data, { headers: authHeader() })
    ).data;
    return res;
  },
};
