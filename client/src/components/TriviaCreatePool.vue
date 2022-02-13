<template lang="pug">
v-card 
  v-card-text
    v-text-field(
      v-model="name",
      label="Trivia Name",
      required
    )
  v-divider
  v-card-actions
    v-spacer
    v-btn(text @click="createTrivia") Create Trivia Pool Test

        



</template>

<script>
import axios from "axios";
export default {
  name: "TriviaCreatePool",

  data: () => ({
    name: "",
  }),
  methods: {
    async createTrivia() {
      const trivia = { name: this.name };
      const newTrivia = (
        await axios.post("http://localhost:5000/api/trivias/", trivia)
      ).data.trivia;
      this.name = "";
      this.$emit("new", newTrivia);
    },
  },
};
</script>
