<template lang="pug">
 #NotificationList
     Notification( v-for="notification in notifications" :notification="notification" :key="notification.message").notification
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "NotificationList",
  components: {
    Notification: () => import("./Notification.vue"),
  },
  computed: {
    ...mapGetters({
      notifications: "notifications/notifications",
    }),
  },
};
</script>

<style scoped></style>
