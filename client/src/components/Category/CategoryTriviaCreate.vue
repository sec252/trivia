<template lang="pug">
v-dialog(
  transition="dialog-bottom-transition"
  max-width="600"
  v-model="dialog"
)
  v-card(
    flat
    tile
  )
    v-toolbar(
      :elevation="1"
      color="primary"
      dark
    ).mb-2 
      v-icon.mr-3 {{icon}}
      v-toolbar-title {{title}}
      v-spacer
      v-btn(icon @click="$emit('cancel')")
        v-icon mdi-close

    v-card-text
        v-text-field(
            v-model="name",
            label="Trivia Name",
            required
        )
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
    #card(v-if="questions.length > 0")
        v-row( no-gutters).pl-6
            v-col(cols=5): p Questions
            v-col(cols=5): p Answers
            v-col(cols=2): p Actions
        template(v-for="question in questions")
            v-row(:key="question.text" no-gutters).pl-6
                v-col(cols=5): p {{question.text}}
                v-col(cols=5): p {{question.answer}}
                v-col(cols=2)
                    v-tooltip(bottom).mt-2
                        template(v-slot:activator='{ on, attrs }')
                            v-icon(color='error' dark v-bind='attrs' v-on='on'
                            @click="deleteQuestion(question.text)"
                            )
                                | mdi-delete
                        span Delete Triva Question
    v-divider
    v-card-actions
        v-spacer
        v-btn(color='error' text @click='$emit("cancel")')
            | Cancel
        v-btn(color='primary' @click="save"  )
            | Save
</template>

<script>
import { TriviaAPI } from "../../services/trivia";
export default {
  name: "CategoryTriviaCreate",
  props: {
    dialog: {
      type: Boolean,
      required: true,
    },
    category: {
      type: Object,
      required: false,
      default: () => {},
    },
  },
  data: () => ({
      name: "",
      newQuestion: "",
      newAnswer: "",
      questions:[]
  }),
  computed: {
    title() {
      return this.category.name
    },
    icon() {
      return "mdi-shapes"
    },
  },
  methods: {
    async addQuestion() {
      const data = {
        text: this.newQuestion,
        answer: this.newAnswer,
      };

      this.questions.push(data)
      this.newQuestion = "";
      this.newAnswer = "";
    },
    async deleteQuestion(text) {
      this.questions = this.questions.filter(
        (q) => q.text !== text
      );
    },
    async save() {
        const trivia = {
          name: this.name,
          category_id: this.category.id,
        };
        const newTrivia = (await TriviaAPI.createTrivia(trivia)).trivia;

        if(newTrivia) {
            for (let q of this.questions) {
                await TriviaAPI.createTriviaPoolQuestions(newTrivia.id, q)
            }
        }
        
      this.name =  "";
      this.newQuestion = "";
      this.newAnswer = "";
      this.questions = [];
      this.$emit("reload");
    },
  },
};
</script>

<style scoped>
#card {
  max-height: 400px;
  overflow-y: auto;
}

#card::-webkit-scrollbar-track {
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}

#card::-webkit-scrollbar-thumb {
  background-color: indigo !important;
  outline: 1px solid indigo !important;
}
</style>