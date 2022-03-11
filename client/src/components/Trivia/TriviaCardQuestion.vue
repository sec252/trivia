<template lang="pug">
v-expand-transition
  v-card.mx-auto(:color='show ? "success" : "info"' dark minHeight="180px" width='500px')
    v-card-title
      span.text-h6.font-weight-light {{number + 1}}/{{total}}
    v-card-text.text-h5.font-weight-bold.white--text
      | {{show ? answer : text}}
    v-card-actions
      v-row( no-gutters).mb-2
        v-btn(outlined color="white" @click="showAnswer").ml-2 Show answer
        v-spacer
        v-btn(outlined color="white" @click="$emit('next'); show=false;").mr-2 Next

</template>

<script>
export default {
  name: "TriviaCardQuestion",
  props: {
    number: {
      type: Number,
      required: true,
      default: 1,
    },
    text: {
      type: String,
      required: true,
      default: "test",
    },
    answer: {
      type: String,
      required: true,
      default: "answer",
    },
    total: {
      type: Number,
      required: true,
      default: 1,
    },
  },
  data: () => ({
    show: false,
  }),
  methods: {
    showAnswer() {
      this.show = !this.show;
    },
  },
};
</script>
