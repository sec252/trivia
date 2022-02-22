<template lang="pug">
  v-app
    TheNavBar
    v-main
      router-view

</template>

<script>
export default {
  name: "App",
  components: {
    TheNavBar: () => import("./components/Navbar/TheNavBar.vue"),
  },
  data: () => ({
    //
  }),
};
</script>
