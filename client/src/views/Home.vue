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
    FilterBtn(@order="orderBy")

    TriviaList(:trivias="filteredSearch")
</template>

<script>
import { TriviaAPI } from "../services/trivia";
export default {
  name: "Home",
  components: {
    TriviaList: () => import("../components/Trivia/TriviaList.vue"),
    FilterBtn: () => import("../components/Filter/FilterBtn.vue"),
  },
  data: () => ({
    triviaPools: [],
    filteredSearch: [],
    search: "",
    page: 1,
    perPage: 10,
    order: "most",
  }),
  beforeMount() {
    this.getTrivias();
  },
  mounted() {
    this.getNextTrivia();
  },
  methods: {
    async getTrivias() {
      this.triviaPools = (
        await TriviaAPI.getTriviaCollection(this.page, this.perPage, this.order)
      ).items;
      this.filteredSearch = this.triviaPools;
    },
    async getNextTrivia() {
      window.onscroll = async () => {
        let bottomOfWindow =
          document.documentElement.scrollTop + window.innerHeight ===
          document.documentElement.offsetHeight;
        if (bottomOfWindow) {
          this.page++;
          const res = (
            await TriviaAPI.getTriviaCollection(
              this.page,
              this.perPage,
              this.order
            )
          ).items;
          this.triviaPools = [...this.triviaPools, ...res];
          this.filteredSearch = this.triviaPools;
        }
      };
    },
    orderBy(order) {
      this.triviaPools = [];
      this.page = 1;
      this.perPage = 10;
      this.order = order;
      this.getTrivias();
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
