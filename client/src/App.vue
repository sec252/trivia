<template lang="pug">
  v-app
    template(v-for="notification in notifications")
      Notification(:notification="notification")
    TheNavBar
    v-main
      router-view

</template>

<script>
import { mapActions,mapGetters } from "vuex";
export default {
  name: "App",
  components: {
    TheNavBar: () => import("./components/Navbar/TheNavBar.vue"),
    Notification: () => import("./components/Notifications/Notification.vue"),
  },
  data: () => ({
    //
  }),

  computed: {
    ...mapGetters({
      notifications: "notifications/notifications",
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
