<template lang="pug">
  v-row(dense no-gutters)
    v-col(v-for="trivia in trivias" cols=12 md=6 :key="trivia.id").pa-2
      TriviaCard( :title="trivia.name", :timestamp="trivia.createdDate", :plays="trivia.plays" :author="trivia.author.username")
</template>

<script>
export default {
  name: "TriviaList",
  components: {
    TriviaCard: () => import("./TriviaCard.vue"),
  },
  props: {
    trivias: {
      type: Array,
      required: true,
      default: () => [],
    },
  },
};
</script>
