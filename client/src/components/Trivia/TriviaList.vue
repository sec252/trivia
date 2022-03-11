<template lang="pug">
  v-row(dense no-gutters)
    v-col(v-for="trivia in trivias" cols=12 md=6 :key="trivia.id").pa-2
      TriviaCard(
        :id="trivia.id" 
        :title="trivia.name", 
        :timestamp="trivia.createdDate", 
        :plays="trivia.plays" 
        :author="trivia.author.username"
        @play="playTrivia"
      )
    TriviaCardPlay(
      :triviaId="this.triviaId" 
      :dialog="dialog"
      :key="dialog"
      @cancel="dialog=false"
    )
</template>

<script>
export default {
  name: "TriviaList",
  components: {
    TriviaCard: () => import("./TriviaCard.vue"),
    TriviaCardPlay: () => import("./TriviaCardPlay.vue"),
  },
  props: {
    trivias: {
      type: Array,
      required: true,
      default: () => [],
    },
  },
  data: () => ({
    triviaId: null,
    dialog: false,
  }),
  methods: {
    playTrivia(id) {
      this.triviaId = id;
      this.dialog = true;
    },
  },
};
</script>
