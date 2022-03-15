<template lang="pug">
v-snackbar#snackbar(:timeout='-1' :value='true' :color="notification.type"   shaped ).text-center
  span.white--text {{notification.message}}
  
</template>

<script>
export default {
  name: "Notification",
  props: {
    notification: Object,
  },
};
</script>

<style scoped>
#snackbar {
  z-index: 2000 !important;
}
</style>
