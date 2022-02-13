<template lang="pug">
.text-center
  v-dialog(v-model='dialog' width='500')
    v-card
      v-card-title.text-h5.grey.lighten-2
        | {{user.username}}
      v-card-text.pt-4
        p(v-if="user.active").green--text This user is active
        p(v-else).red--text This user is not active
      v-divider
      v-card-actions
        v-spacer
        v-btn(color='primary' text @click='$emit("cancel")')
          | okay

</template>

<script>
export default {
  name: "UserDetailsDialog",
  props: {
    dialog: {
      type: Boolean,
    },
    user: {
      type: Object,
    },
  },
};
</script>
