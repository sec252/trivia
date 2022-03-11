<template lang="pug">
.text-center
  v-dialog(v-model='dialog' width='600')
    v-card
      v-card-title.text-h5
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
              span Add Question
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
import { TriviaAPI } from "../../services/trivia";
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
        await TriviaAPI.createTriviaPoolQuestions(this.triviaPool.id, data)
      ).question;

      this.triviaPool.questions.push(newQ);
      this.newQuestion = "";
      this.newAnswer = "";
    },
    async deleteQuestion(id) {
      await TriviaAPI.deleteTriviaQuestionItem(id);

      this.triviaPool.questions = this.triviaPool.questions.filter(
        (q) => q.id !== id
      );
    },
    async save(id) {
      const triviaPool = {
        name: this.triviaPool.name,
      };

      const editedTriviaPool = (await TriviaAPI.editTriviaItem(id, triviaPool))
        .trivia;

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
