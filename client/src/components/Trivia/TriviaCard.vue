<template lang="pug">
div
  v-card(:color='color' dark)
    v-row(no-gutters)
      v-col(cols=8)
        v-card-title.text-h5 {{trivia.name}}
        v-card-subtitle
          | Created {{date}}
      v-col(cols=4).text-center
        .text-h5.mt-3 {{trivia.plays}}
        v-card-subtitle.pt-0
          | Total Plays
    v-card-actions
      v-row(no-gutters)
        v-col(cols=8)
          v-btn(text @click="$emit('play', trivia.id)")
            v-icon(left)
              | mdi-play
            | Play
        v-col(cols=4).text-center
          p.mt-2
              | Author: {{trivia.author.username}}

</template>

<script>
import moment from "moment";
export default {
  name: "TriviaCard",
  props: {
    trivia: {
      type: Object,
      required: true,
    },
  },
  computed: {
    date() {
      var ts = new Date(this.trivia.createdDate);
      const local = this.convertUTCDateToLocalDate(ts);
      const time = moment(local, "YYYYMMDD").fromNow();
      return time;
    },
    color() {
      if (this.plays < 20) {
        return "blue darken-4";
      } else if (this.plays >= 20 && this.plays < 60) {
        return "deep-orange darken-4";
      }

      return "teal darken-4";
    },
  },
  methods: {
    convertUTCDateToLocalDate(date) {
      var newDate = new Date(
        date.getTime() + date.getTimezoneOffset() * 60 * 1000
      );

      var offset = date.getTimezoneOffset() / 60;
      var hours = date.getHours();

      newDate.setHours(hours - offset);

      return newDate;
    },
  },
};
</script>
