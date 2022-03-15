import { apiService } from "@/api";
import authHeader from "@/services/auth-header";
export const TriviaAPI = {
  getTriviaCollection: async () => {
    const res = (await apiService.get("/trivias/")).data;
    return res;
  },
  getTriviaCategoryCollection: async (id) => {
    const res = (await apiService.get("/trivias/category/" + id)).data;
    return res;
  },
  getTriviaPoolQuestions: async (id) => {
    const res = (await apiService.get("/trivias/" + id + "/questions")).data;
    return res;
  },
  getTriviaUserCollection: async () => {
    const res = (
      await apiService.get("/trivias/user", { headers: authHeader() })
    ).data;
    return res;
  },
  createTrivia: async (data) => {
    const res = (
      await apiService.post("/trivias/", data, { headers: authHeader() })
    ).data;
    return res;
  },
  createTriviaPoolQuestions: async (id, data) => {
    const res = (
      await apiService.post("/trivias/" + id + "/questions", data, {
        headers: authHeader(),
      })
    ).data;
    return res;
  },
  getTriviaItem: async (id) => {
    const res = (await apiService.get("/trivias/" + id)).data;
    return res;
  },
  editTriviaItem: async (id, data) => {
    const res = (
      await apiService.put("/trivias/" + id, data, { headers: authHeader() })
    ).data;
    return res;
  },
  updateTriviaPlays: async (id, data) => {
    const res = (await apiService.put(`/trivias/${id}/plays`, data)).data;

    return res.body;
  },
  deleteTriviaItem: async (id) => {
    await apiService.delete("/trivias/" + id, {
      headers: authHeader(),
    });
  },
  deleteTriviaQuestionItem: async (id) => {
    await apiService.delete("/trivias/questions/" + id, {
      headers: authHeader(),
    });
  },
};
