<template lang="pug">
v-row(no-gutters)
  v-col.py-2(cols='12').text-center
    v-btn-toggle(v-model='icon' borderless rounded)
      v-btn(small value='asc')
        span.hidden-sm-and-down Ascending
        v-icon(right)
          | mdi-sort-alphabetical-ascending
      v-btn(small value='desc')
        span.hidden-sm-and-down Descending
        v-icon(right)
          | mdi-sort-alphabetical-descending
      v-btn(small value='most')
        span.hidden-sm-and-down Most Played
        v-icon(right)
          | mdi-sort-numeric-ascending-variant
      v-btn(small value='least')
        span.hidden-sm-and-down Least Played
        v-icon(right)
          | mdi-sort-numeric-descending-variant
      v-btn(small value='newest')
        span.hidden-sm-and-down Newest
        v-icon(right)
          | mdi-sort-clock-ascending-outline
      v-btn(small value='oldest')
        span.hidden-sm-and-down Oldest
        v-icon(right)
          | mdi-sort-clock-descending-outline


</template>

<script>
export default {
  name: "FilterBtn",
  data: () => ({
    icon: "most",
  }),
  watch: {
    icon: function handleChange(val) {
      this.$emit("order", val);
    },
  },
};
</script>
