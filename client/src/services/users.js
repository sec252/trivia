import { apiService } from "@/api";
import authHeader from "@/services/auth-header";
export const UsersAPI = {
  getUserCollection: async () => {
    const res = (await apiService.get("/users/", { headers: authHeader() }))
      .data;
    return res;
  },
  createUser: async (data) => {
    const res = (
      await apiService.post("/users/", data, { headers: authHeader() })
    ).data;
    return res;
  },
  getUserItem: async (id) => {
    const res = (
      await apiService.get("/users/" + id, { headers: authHeader() })
    ).data;
    return res;
  },
  editUserItem: async (id, data) => {
    const res = (
      await apiService.put("/users/" + id, data, {
        headers: authHeader(),
      })
    ).data;

    return res;
  },
  deleteUserItem: async (id) => {
    await apiService.delete("/users/" + id, {
      headers: authHeader(),
    });
  },
};
