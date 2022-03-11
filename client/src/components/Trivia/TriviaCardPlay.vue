<template lang="pug">
.text-center
  v-dialog(v-model='dialog' fullscreen)
    v-card
      v-toolbar(dark :color='end ? "warning" : "info"')
        v-btn(icon dark @click='$emit("cancel")')
          v-icon mdi-close
        v-toolbar-title {{trivia.name}} Trivia
        v-spacer
      v-card-text.pt-4.text-center
        v-btn#start( 
          rounded 
          color="info"
          @click="startTrivia"
          v-if="start"
        ) Start
        template(v-for="(q, i) in trivia.questions" v-if="!start")
          TriviaCardQuestion(
            :number="i", 
            :text="q.text"
            :answer="q.answer"
            :total="trivia.questions.length"
            v-if="q.text == current"
            @next="updateNext"
          )
        v-btn#end( 
          rounded 
          color="warning"
          @click="startTrivia"
          v-if="end"
        ) Restart



</template>

<script>
import { TriviaAPI } from "../../services/trivia";
import TriviaCardQuestion from "./TriviaCardQuestion.vue";
export default {
  name: "TriviaCardPlay",
  components: {
    TriviaCardQuestion,
  },
  props: {
    dialog: {
      type: Boolean,
    },
    triviaId: {
      type: Number,
    },
  },
  data: () => ({
    trivia: {},
    current: "",
    start: true,
    end: false,
    next: 0,
    questions: [],
  }),
  created() {
    if (this.triviaId !== null) this.getTrivia(this.triviaId);
  },
  methods: {
    async getTrivia(id) {
      const res = (await TriviaAPI.getTriviaItem(id)).trivia;
      this.trivia = res;
    },
    startTrivia() {
      this.end = false;
      this.start = false;
      this.trivia?.questions.forEach((q) => {
        this.questions.push(q.text);
      });
      this.current = this.questions[this.next];
    },
    updateNext() {
      this.next++;
      this.current = this.questions[this.next];
      if (this.next == this.questions.length) {
        setTimeout(() => {
          this.end = true;
        }, 500);
      }
    },
  },
};
</script>

<style scoped>
.v-card__text {
  height: 90vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
#start {
  width: 500px;
  height: 300px !important;
  font-size: 5rem;
}
#end {
  width: 500px;
  height: 300px !important;
  font-size: 5rem;
}
</style>
