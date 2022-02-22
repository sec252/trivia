<template lang="pug">
  HelloWorld
</template>

<script>
export default {
  name: "Admin",
  components: {
    HelloWorld: () => import("../components/HelloWorld.vue"),
  },
};
</script>
