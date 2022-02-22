<template lang="pug">
  v-container
    v-row
      v-col(cols=12 md=6)
        h1.mt-3 All Trivias
      v-col(cols=12 md=6)
        v-text-field(
          label="Search Trivia Pools"
          prepend-icon="mdi-magnify"
        )
    TriviaList(:trivias="triviaPools")
</template>

<script>
import axios from "axios";
export default {
  name: "Home",
  components: {
    TriviaList: () => import("../components/Trivia/TriviaList.vue"),
  },
  data: () => ({
    triviaPools: [],
  }),
  created() {
    this.getTrivias();
  },
  methods: {
    async getTrivias() {
      const trivias = await axios.get("http://localhost:5000/api/trivias/");
      this.triviaPools = trivias.data?.body;
    },
  },
};
</script>
