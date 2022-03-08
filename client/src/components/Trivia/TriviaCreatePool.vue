<template lang="pug">
v-card 
  v-card-text
    v-text-field(
      v-model="name",
      label="Trivia Name",
      required
    )
    v-autocomplete(
      v-model="select"
      :items="items",
      item-text="name"
      item-value="id"
      label="Catagories",
      required
    )
  v-divider
  v-card-actions
    v-spacer
    v-btn(text @click="createTrivia") Create Trivia Pool

        



</template>

<script>
import { CategoriesAPI } from "../../services/category";
import { TriviaAPI } from "../../services/trivia";
export default {
  name: "TriviaCreatePool",

  data: () => ({
    name: "",
    select: null,
    items: [],
  }),
  async created() {
    this.items = (await CategoriesAPI.getCategoryCollection()).categories;
  },
  methods: {
    async createTrivia() {
      const trivia = {
        name: this.name,
        category_id: this.select,
      };
      const newTrivia = (await TriviaAPI.createTrivia(trivia)).trivia;
      this.name = "";
      this.select = null;
      this.$emit("new", newTrivia);
    },
  },
};
</script>
