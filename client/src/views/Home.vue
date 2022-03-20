<template lang="pug">
  v-container
    v-card(:color="$vuetify.theme.dark ? '#121212': 'white'" flat).sticky.mb-2.py-3: v-row
      v-col(cols=12).text-center
        h1.mt-3 {{title}} 
      FilterBtn(@order="orderBy")
      v-col(cols=12 lg=4)
        v-text-field(
          label="Search Trivias"
          placeholder="Try Splitgate"
          prepend-icon="mdi-magnify"
          autofocus
          v-model="search"
          )
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
    slug: "",
    title: "Most Played Trivias",
  }),
  watch: {
    search: function handleSearch(val) {
      this.search = val;
      this.getTrivias();
    },
  },
  beforeMount() {
    this.getTrivias();
  },
  mounted() {
    this.getNextTrivia();
  },
  methods: {
    async getTrivias() {
      this.triviaPools = (
        await TriviaAPI.getTriviaCollection(
          this.slug,
          this.search,
          this.page,
          this.perPage,
          this.order
        )
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
              this.slug,
              this.search,
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
      this.setTitle(order);
      this.triviaPools = [];
      this.page = 1;
      this.perPage = 10;
      this.order = order;
      this.getTrivias();
    },
    setTitle(order) {
      switch (order) {
        case "asc":
          this.title = "Sorted Trivias By Ascending Order";
          break;
        case "desc":
          this.title = "Sorted Trivias By Descending Order";
          break;
        case "least":
          this.title = "Least Played Trivias";
          break;
        case "newest":
          this.title = "Most Recent Trivias";
          break;
        case "oldest":
          this.title = "Oldest Trivias";
          break;
        case "most":
          this.title = "Most Played Trivias";
      }
    },
  },
};
</script>

<style scoped>
.sticky {
  position: -webkit-sticky; /* Safari */
  position: sticky;
  top: 64px;
  z-index: 2;
  overflow: hidden;
}
</style>
