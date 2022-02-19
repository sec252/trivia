<template lang="pug">
.text-center
  v-dialog(v-model='dialog' width='600')
    v-card
      v-card-title.text-h5.grey.lighten-2
        | {{triviaPool.name}}
      v-card-text
        v-text-field(v-model="triviaPool.name", label="Name").mt-2
        v-row(no-gutters)
          v-col(cols=12)
            v-text-field(v-model="newQuestion", label="Enter Question").mt-2
          v-col(cols=12, md=10)
            v-text-field(v-model="newAnswer", label="Enter Answer").mt-2
          v-col(cols=12, md=2)
            v-tooltip(bottom).mt-2
              template(v-slot:activator='{ on, attrs }')
                v-icon(color='success' dark v-bind='attrs' v-on='on'
                @click="addQuestion"
                ).ml-10.mt-6
                  | mdi-plus
              span Edit User
      #card
        v-row( no-gutters).pl-6
          v-col(cols=5): p Questions
          v-col(cols=5): p Answers
          v-col(cols=2): p Actions
        template(v-for="question in triviaPool.questions")
          v-row(:key="question.id" no-gutters).pl-6
            v-col(cols=5): p {{question.text}}
            v-col(cols=5): p {{question.answer}}
            v-col(cols=2)
              v-tooltip(bottom).mt-2
                template(v-slot:activator='{ on, attrs }')
                  v-icon(color='error' dark v-bind='attrs' v-on='on'
                  @click="deleteQuestion(question.id)"
                  )
                    | mdi-delete
                span Delete Triva Question
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
  data: () => ({
    newQuestion: "",
    newAnswer: "",
  }),
  methods: {
    async addQuestion() {
      const data = {
        text: this.newQuestion,
        answer: this.newAnswer,
      };

      const newQ = (
        await axios.post(
          `http://localhost:5000/api/trivias/${this.triviaPool.id}/questions`,
          data
        )
      ).data.question;

      this.triviaPool.questions.push(newQ);
    },
    async deleteQuestion(id) {
      await axios.delete(`http://localhost:5000/api/trivias/questions/${id}`);

      this.triviaPool.questions = this.triviaPool.questions.filter(
        (q) => q.id !== id
      );
    },
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

<style scoped>
#card {
  min-height: 300px;
  max-height: 500px;
  overflow-y: auto;
}

#card::-webkit-scrollbar-track {
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}

#card::-webkit-scrollbar-thumb {
  background-color: darkgrey;
  outline: 1px solid slategrey;
}
</style>
