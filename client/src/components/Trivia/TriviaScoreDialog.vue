<template lang="pug">
.text-center
  v-dialog(v-model='dialog' width='600')
    v-card
      v-card-title.text-h5
        | {{title}}
      v-card-text
        p Wrong: {{scoreDetails.wrong}}
        p Correct: {{scoreDetails.correct}}
        p Played: {{scoreDetails.date}}
        
      v-divider
      v-card-actions
        v-spacer
        v-btn(color='info' text @click='$emit("cancel")')
          | Go Back
        v-btn(color='primary' text @click='$emit("restart")')
          | Restart

</template>

<script>
export default {
  name: "TriviaScoreDialog",
  props: {
    dialog: {
      type: Boolean,
    },
    scoreDetails: {
      type: Object,
    },
  },
  data: () => ({}),
  computed: {
    title() {
      const score = this.scoreDetails.score;
      if (score == 0) return "Go Kill Yourself";
      if (score < 50) return "Man You Are Fucking Dumb";
      if (score > 50 && score < 80) return "Not Bad!";
      if (score > 80 && score < 99) return "Almost Perfect!";
      return "You Fucking Tryhard!";
    },
  },
  methods: {},
};
</script>
