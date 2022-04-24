<template lang="pug">
.text-center
  v-dialog(v-model='dialog' width='600')
    v-card
      v-toolbar(
        :elevation="1"
        color="primary"
        dark
      ).mb-2 
        v-icon.mr-3 mdi-calculator-variant-outline
        v-toolbar-title {{title}}
        v-spacer
        v-btn(icon @click="$emit('cancel')")
          v-icon mdi-close
      v-card-text
        v-row(no-gutters)
          v-col(cols=6)
            p.mt-4 Wrong: {{scoreDetails.wrong}}
            p Correct: {{scoreDetails.correct}}
            p Played: {{scoreDetails.date}}
          v-col(cols=6).d-flex.flex-column.justify-center.align-center
            h1 {{scoreDetails.score}}%
      v-divider
      v-card-actions
        v-spacer
        v-btn( text @click='$emit("cancel")')
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
      if (score <= 50) return "Man You Are Fucking Dumb";
      if (score > 50 && score < 80) return "Not Bad!";
      if (score >= 80 && score < 99) return "Almost Perfect!";
      return "You Fucking Tryhard!";
    },
  },
  methods: {},
};
</script>
