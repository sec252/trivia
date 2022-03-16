<template lang="pug">
  v-app
    NotificationList
    TheNavBar
    v-main.mt-10
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
