<template lang="pug">
  AdminHome
</template>

<script>
export default {
  name: "Admin",
  components: {
    AdminHome: () => import("../components/Admin/AdminHome.vue"),
  },
};
</script>
