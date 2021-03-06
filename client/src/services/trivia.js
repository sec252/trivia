import { apiService } from "@/api";
import authHeader from "@/services/auth-header";
export const TriviaAPI = {
  getTriviaCollection: async (
    slug = null,
    search = null,
    page = 1,
    perPage = 5,
    order = "most"
  ) => {
    const res = (
      await apiService.get(
        `/trivias/?slug=${slug}&search=${search}&page=${page}&perPage=${perPage}&order=${order}`
      )
    ).data;
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
    const res = (
      await apiService.put(`/trivias/${id}/plays`, data, {
        headers: authHeader(),
      })
    ).data;

    return res.body;
  },
  createTriviaScore: async (id, data) => {
    const res = (
      await apiService.post(`/trivias/${id}/score`, data, {
        headers: authHeader(),
      })
    ).data;

    return res;
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
  answerTrivia: async (id, data) => {
    const res = (
      await apiService.put(`/trivias/${id}/answer`, data, {
        headers: authHeader(),
      })
    ).data;
    return res;
  },
};
