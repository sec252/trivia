<template lang="pug">
v-container
  v-row.pa-2
    v-col(cols=12 md=6)
      v-row
        h1.mt-5.ml-3 Categories
        v-spacer
        v-btn.mt-6.mr-3(
          tile 
          color='success' 
          @click="dialog=true"
          v-if="hasAccess"
        )
          v-icon(left)
            | mdi-plus
          | New Category
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
      sm=6
      md=4
      lg=3 
      v-for="category in filteredCategories" 
      :key="category.id + rerender"
    )
      CategoryCard(:category="category" @new="newTrivia")
    CategoryCreateForm(:dialog="dialog" :key="dialog" @cancel="dialog=false" @new="addCategory") 
    CategoryTriviaCreate(:dialog="newTriviaDialog" :category="category" @cancel="newTriviaDialog = false" @reload="newTriviaDialog=false; rerender++;" )
</template>

<script>
import { CategoriesAPI } from "../services/category";
import CategoryCard from "../components/Category/CategoryCard.vue";
import CategoryCreateForm from "../components/Category/CategoryCreateForm.vue";
import CategoryTriviaCreate from "../components/Category/CategoryTriviaCreate.vue";
import { mapGetters } from "vuex";
export default {
  name: "Categories",
  components: {
    CategoryCard,
    CategoryCreateForm,
    CategoryTriviaCreate,
  },
  data: () => ({
    dialog: false,
    newTriviaDialog: false,
    categories: [],
    rerender: 1,
    filteredCategories: [],
    select: null,
    category: {},
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
  computed: {
    ...mapGetters({
      authUser: "auth/user",
    }),
    hasAccess() {
      if (this.authUser && this.authUser.role == "admin") {
        return true;
      }
      return false;
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
    addCategory(category) {
      this.categories.push(category);
      this.filteredCategories = this.categories;
    },
    newTrivia(catId) {
      this.category = this.categories.find((c) => c.id == catId);
      this.newTriviaDialog = true;
    },
  },
};
</script>
