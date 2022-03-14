<template lang="pug">
.text-center
  v-dialog(v-model='dialog' width='500')
    v-card
      v-card-title.text-h5.grey.lighten-2
        | New Category
      v-card-text
       v-text-field(v-model="category", label="Enter Category")
       
      v-divider
      v-card-actions
        v-spacer
        v-btn(color='error' text @click='$emit("cancel")')
          | Cancel
        v-btn(color='primary' text @click='save')
          | Save

</template>

<script>
import { CategoriesAPI } from "../../services/category";
import { mapActions } from "vuex";
export default {
  name: "CategoryCreateForm.vue",
  props: {
    dialog: {
      type: Boolean,
    },
  },
  data: () => ({
      category: ""
  }),
  methods: {
    ...mapActions({
      addNotification: "notifications/addNotification",
    }),
    async save() {
        try {
            const data = {
                name: this.category,
            };
            const newCategory = (await CategoriesAPI.createCategory(data)).category
            this.addNotification(
                {
                    message: "This worked and a notification was added",
                    type: "success"
                }
            )
            this.$emit("new", newCategory);
            this.$emit("cancel");
        } catch (error) {
            console.error(error.response.data);
            this.addNotification(
                {
                    message: error.response?.data?.message,
                    type: "error"
                }
            )
        }
    },
  },
};
</script>
