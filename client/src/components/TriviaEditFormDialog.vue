<template lang="pug">
.text-center
  v-dialog(v-model='dialog' width='500')
    v-card
      v-card-title.text-h5.grey.lighten-2
        | {{triviaPool.name}}
      v-card-text
       v-text-field(v-model="triviaPool.name", label="Name")
       
      v-divider
      v-card-actions
        v-spacer
        v-btn(color='error' text @click='$emit("cancel")')
          | Cancel
        v-btn(color='primary' text @click='save(triviaPool.id)')
          | Save

</template>

<script>
import axios from "axios";
export default {
  name: "TriviaEditFormDialog",
  props: {
    dialog: {
      type: Boolean,
    },
    triviaPool: {
      type: Object,
    },
  },
  methods: {
    async save(id) {
      const triviaPool = {
        name: this.triviaPool.name,
      };

      const editedTriviaPool = (
        await axios.put(`http://localhost:5000/api/trivias/${id}`, triviaPool)
      ).data?.trivia;
      console.log(editedTriviaPool);
      this.$emit("updateTrivia", editedTriviaPool);
      this.$emit("cancel");
    },
  },
};
</script>
