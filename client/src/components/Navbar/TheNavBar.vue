<template lang="pug">
div
  v-app-bar(fixed)
    v-toolbar-title#title Trivia App
    v-spacer
    v-btn(text to="/admin" v-if="isAuth") My Trivias
    v-btn(text to="/about") About
    v-btn(text to="/") Trivias
    v-btn(text to="/categories") Categories
    v-menu(left bottom)
      template(v-slot:activator='{ on, attrs }')
        v-btn(icon v-bind='attrs' v-on='on')
          v-icon mdi-cog
      v-list(:key="darkMode")
        v-list-item-group(
          v-model="selectedItem"
          color="default"
        )
          v-list-item(
            v-for='(item, i) in menu' 
            :key='i'
            @click="item.func"
            v-if="showIfAuth(item.isAuth)"
          )
            v-list-item-icon
              v-icon {{item.icon}}
            v-list-item-content
              v-list-item-title(
                :key="item.title"
                v-text='item.title'
              )
          v-list-item(
            @click="toggleDarkMode"
            v-if="showIfAuth(null)"
          )
            v-list-item-icon
              v-icon mdi-theme-light-dark
            v-list-item-content
              v-list-item-title(
                v-text='modeTitle'
              )
  AuthDialog(
    :dialog="dialog"
    @cancel="dialog=false"
    :register="register"
    :key="dialog"
  )



</template>

<script>
import { mapActions, mapGetters } from "vuex";
import AuthDialog from "../Auth/AuthDialog.vue";
export default {
  name: "TheNavBar",
  components: {
    AuthDialog,
  },
  data: (v) => ({
    dialog: false,
    selectedItem: 1,
    register: false,
    darkMode: false,
    modeTitle: "Dark Mode",
    menu: [
      {
        icon: "mdi-account-plus",
        title: "Register",
        func: v.handleRegister,
        isAuth: false,
      },
      {
        icon: "mdi-login",
        title: "Login",
        func: v.handleLogin,
        isAuth: false,
      },
      {
        icon: "mdi-logout",
        title: "Logout",
        func: v.handleLogout,
        isAuth: true,
      },
      {
        icon: "mdi-account-details",
        title: "Account Details",
        func: v.handleLogin,
        isAuth: true,
      },
    ],
  }),
  watch: {
    darkMode: function handleModeTitle(val) {
      val ? (this.modeTitle = "Light Mode") : (this.modeTitle = "Dark Mode");
    },
  },
  computed: {
    ...mapGetters({
      authUser: "auth/user",
      isAuth: "auth/isLoggedIn",
    }),
  },
  mounted() {
    if (localStorage.getItem("darkMode")) {
      this.darkMode = JSON.parse(localStorage.getItem("darkMode"));
      this.$vuetify.theme.dark = this.darkMode;
    } else {
      localStorage.setItem("darkMode", this.darkMode);
    }
  },
  methods: {
    ...mapActions({
      logout: "auth/logoutUser",
    }),
    menuItems() {
      return this.menu;
    },
    toHome() {
      this.$router.push("/");
    },
    showIfAuth(show) {
      if (show == null) return true;
      if (show && this.isAuth) {
        return true;
      } else if (!show && !this.isAuth) {
        return true;
      }
      return false;
    },
    handleLogin() {
      this.register = false;
      this.dialog = true;
    },
    toggleDarkMode() {
      this.$vuetify.theme.dark = !this.$vuetify.theme.dark;
      this.darkMode = this.$vuetify.theme.dark;
      localStorage.setItem("darkMode", this.$vuetify.theme.dark);
    },
    handleRegister() {
      this.register = true;
      this.dialog = true;
    },
    async handleLogout() {
      try {
        this.logout();
        if (this.$router.history?.current?.name != "Home") {
          this.toHome();
        }
      } catch (error) {
        console.error(error);
      }
    },
  },
};
</script>

<style scoped>
#title {
  cursor: pointer;
}
</style>
