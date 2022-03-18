<template lang="pug">
v-card
  v-img.white--text.align-end(:src='category.img_url' gradient='to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)' height='200px')
    v-card-title(v-text='category.name')
  v-card-actions
    v-spacer
      v-btn.ml-auto(
        outlined 
        small
        :to="'/categories/'+ category.slug"
      )
        v-icon(left)
          | mdi-magnify
        | Explore

</template>

<script>
export default {
  name: "CatergoryCard",
  props: {
    category: {
      type: Object,
      required: true,
    },
  },
};
</script>
