<template lang="pug">
  v-app#triviaApp
    NotificationList
    TheNavBar
    v-main.mt-15
      router-view

</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "App",
  components: {
    TheNavBar: () => import("./components/Navbar/TheNavBar.vue"),
    NotificationList: () =>
      import("./components/Notifications/NotificationList.vue"),
  },
  data: () => ({
    //
  }),

  computed: {
    ...mapGetters({
      isAuth: "auth/isLoggedIn",
    }),
  },
  methods: {
    ...mapActions({
      getUser: "auth/fetchUser",
    }),
  },
  async created() {
    await this.getUser();
  },
};
</script>

<style>
#triviaApp {
  font-family: "Lato";
}
</style>
