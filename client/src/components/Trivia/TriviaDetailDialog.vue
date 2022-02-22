<template lang="pug">
.text-center
  v-dialog(v-model='dialog' fullscreen)
    v-card
      v-card-title.text-h5.grey.lighten-2
        | {{trivia.name}}
      v-card-text.pt-4
        p TODO: ADD PLAYING TRIVIA FUNCTIONALITY
      v-divider
      v-card-actions
        v-spacer
        v-btn(color='primary' text @click='$emit("cancel")')
          | okay

</template>

<script>
export default {
  name: "TriviaDetailDialog",
  props: {
    dialog: {
      type: Boolean,
    },
    trivia: {
      type: Object,
    },
  },
};
</script>
