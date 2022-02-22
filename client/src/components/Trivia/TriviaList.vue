<template lang="pug">
  v-row(dense no-gutters)
    v-col(v-for="trivia in trivias" cols=12 md=6).pa-2
      TriviaCard(:key="trivia.id" :title="trivia.name", :timestamp="trivia.createdDate")
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
