<template lang="pug">
v-card(:color='color' dark)
  v-row(no-gutters)
    v-col(cols=8)
      v-card-title.text-h5 {{title}}
      v-card-subtitle
        | Created at: {{date}}
    v-col(cols=4).text-center
      .text-h5.mt-3 {{plays}}
      v-card-subtitle.pt-0
        | Total Plays
  v-card-actions
    v-btn(text)
      v-icon(left)
        | mdi-play
      | Play

  
</template>

<script>
export default {
  name: "TriviaCard",
  props: {
    title: {
      type: String,
      required: false,
      default: "asdadsads",
    },
    timestamp: {
      type: String,
      required: false,
      default: "asdadsads",
    },
    plays: {
      type: Number,
      required: false,
      default: 0,
    },
  },
  computed: {
    date() {
      var ts = new Date(this.timestamp);
      return ts.toDateString();
    },
    color() {
      if (this.plays < 10) {
        return "blue darken-4";
      } else if (this.plays > 10 && this.plays < 100) {
        return "deep-orange darken-4";
      }

      return "teal darken-4";
    },
  },
  data: () => ({}),
};
</script>
