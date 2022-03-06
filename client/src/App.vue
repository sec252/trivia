<template lang="pug">
  v-app
    TheNavBar
    v-main
      router-view

</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "App",
  components: {
    TheNavBar: () => import("./components/Navbar/TheNavBar.vue"),
  },
  data: () => ({
    //
  }),
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
