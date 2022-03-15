import { authService } from "@/api";
import authHeader from "@/services/auth-header";
const namespaced = true;

const state = {
  user: {},
  isLoggedIn: false,
};

const getters = {
  isLoggedIn: (state) => state.isLoggedIn,
  user: (state) => state.user,
};

const actions = {
  async registerUser({ dispatch }, user) {
    try {
      const res = (await authService.post("/register", user)).data;
      localStorage.setItem("accessToken", JSON.stringify(res.access_token));
      await dispatch("fetchUser");
    } catch (error) {
      console.log(error);
    }
  },
  async loginUser({ dispatch, commit }, user) {
    try {
      const res = (await authService.post("/login", user)).data;
      localStorage.setItem("accessToken", JSON.stringify(res.access_token));
      await dispatch("fetchUser");
    } catch (error) {
      commit("logoutUserState");
    }
  },
  async fetchUser({ commit }) {
    try {
      const res = (await authService.get("/user", { headers: authHeader() }))
        .data;
      if (res.user) {
        localStorage.setItem("user", JSON.stringify(res.user));
        commit("setUser", res.user);
      }
    } catch (error) {
      console.log(error);
    }
  },
  async logoutUser({ commit }) {
    await authService.post("/logout");
    localStorage.removeItem("accessToken");
    localStorage.removeItem("user");
    commit("logoutUserState");
  },
};

const mutations = {
  setUser(state, user) {
    state.isLoggedIn = true;
    state.user = user;
  },
  logoutUserState(state) {
    state.isLoggedIn = false;
    state.user = {};
  },
};

export default {
  namespaced,
  state,
  getters,
  actions,
  mutations,
};
