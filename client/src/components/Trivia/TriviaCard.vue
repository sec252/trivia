<template lang="pug">
div
  v-card(:color='color' dark)
    v-row(no-gutters)
      v-col(cols=8)
        v-card-title.text-h5 {{title}}
        v-card-subtitle
          | Created on: {{date}}
      v-col(cols=4).text-center
        .text-h5.mt-3 {{plays}}
        v-card-subtitle.pt-0
          | Total Plays
    v-card-actions
      v-row(no-gutters)
        v-col(cols=8)
          v-btn(text @click="$emit('play', id)")
            v-icon(left)
              | mdi-play
            | Play
        v-col(cols=4).text-center
          p.mt-2
              | Author: {{author}}

</template>

<script>
export default {
  name: "TriviaCard",
  props: {
    id: {
      type: Number,
      required: true,
    },
    title: {
      type: String,
      required: false,
      default: "asdadsads",
    },
    author: {
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
      if (this.plays < 20) {
        return "blue darken-4";
      } else if (this.plays >= 20 && this.plays < 100) {
        return "deep-orange darken-4";
      }

      return "teal darken-4";
    },
  },
  data: () => ({}),
};
</script>
