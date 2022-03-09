<template lang="pug">
v-container
  v-row.pa-2
    v-col(
      cols=12 
      md=6 
      v-for="category in categories" 
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
  }),
  async created() {
    this.getCategories();
  },
  methods: {
    async getCategories() {
      this.categories = (
        await CategoriesAPI.getCategoryCollection()
      ).categories;
    },
  },
};
</script>
