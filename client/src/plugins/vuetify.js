import Vue from "vue";
import Vuetify from "vuetify/lib/framework";

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    themes: {
      light: {
        primary: "#3f51b5",
        secondary: "#009688",
        accent: "#9C27B0",
        error: "#f44336",
        warning: "#ff5722",
        info: "#2196f3",
        success: "#4caf50",
      },
      dark: {
        primary: "#7986CB",
        secondary: "#004D40",
        accent: "#4A148C",
        error: "#B71C1C",
        warning: "#BF360C",
        info: "#0D47A1",
        success: "#1B5E20",
      },
    },
  },
});
