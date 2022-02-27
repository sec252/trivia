<template lang="pug">
  v-container
    v-row
      v-col(cols=12 md=6)
        h1.mt-3 All Trivias
      v-col(cols=12 md=6)
        v-text-field(
          label="Search Trivia Pools"
          prepend-icon="mdi-magnify"
          @input="handleSearch"
          v-model="search"
        )
    TriviaList(:trivias="filteredSearch")
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
    filteredSearch: [],
    search: "",
  }),
  created() {
    this.getTrivias();
  },
  methods: {
    async getTrivias() {
      const trivias = await axios.get("http://localhost:5000/api/trivias/");
      this.triviaPools = trivias.data?.body;
      this.filteredSearch = this.triviaPools;
    },
    handleSearch(val) {
      let temp = this.triviaPools;
      if (val !== "") temp = temp.filter((t) => t.name.includes(val));
      this.filteredSearch = temp;
      if (val == "") return;
    },
  },
};
</script>
