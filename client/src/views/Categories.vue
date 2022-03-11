<template lang="pug">
v-container
  v-row.pa-2
    v-col(cols=12 md=6)
      h1.mt-3 Categories
    v-col(cols=12 md=6)
      v-autocomplete(
        label="Search Catergories"
        prepend-icon="mdi-shape-plus"
        :items="categories"
        item-text="name"
        item-value="id"
        v-model="select"
      )
    v-col(
      cols=12 
      md=6 
      v-for="category in filteredCategories" 
      :key="category.id"
    )
      CategoryCard(:category="category")
    

</template>

<script>
import { CategoriesAPI } from "../services/category";
import CategoryCard from "../components/Category/CategoryCard.vue";
export default {
  name: "Categories",
  components: {
    CategoryCard,
  },
  data: () => ({
    categories: [],
    filteredCategories: [],
    select: null,
  }),
  watch: {
    select: function handleSelect(val) {
      this.filteredCategories = this.categories;
      this.filteredCategories = this.filteredCategories.filter(
        (c) => c.id == val
      );
      if (val == "" || val == null) {
        this.filteredCategories = this.categories;
      }
    },
  },
  async created() {
    this.getCategories();
  },
  methods: {
    async getCategories() {
      this.categories = (
        await CategoriesAPI.getCategoryCollection()
      ).categories;
      this.filteredCategories = this.categories;
    },
  },
};
</script>
