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
            :id="q.id",
            :text="q.text"
            :answer="q.answer"
            :total="trivia.questions.length"
            v-if="q.text == current"
            @next="updateNext"
            @prev="updatePrev"
            @addWrong="wrong++"
            @addCorrect="correct++"
          )
        TriviaScoreDialog(
          :dialog="scoreDialog" 
          :scoreDetails="scoreDetails" 
          @cancel="scoreDialog = false; $emit('cancel')" 
          @restart="startTrivia"
        )



</template>

<script>
import { TriviaAPI } from "../../services/trivia";
import TriviaCardQuestion from "./TriviaCardQuestion.vue";
import TriviaScoreDialog from "./TriviaScoreDialog.vue";
import { mapGetters } from "vuex";
export default {
  name: "TriviaCardPlay",
  components: {
    TriviaCardQuestion,
    TriviaScoreDialog,
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
    correct: 0,
    wrong: 0,
    scoreDialog: false,
    scoreDetails: {},
    questions: [],
  }),
  watch: {
    end: async function handleEnd(val) {
      // This is where we make  a call to create a record of a score
      if (val) {
        let userId;
        if (this.authUser.id == undefined) {
          userId = 0;
        } else {
          userId = this.authUser.id;
        }
        const data = {
          userId: userId,
          correct: this.correct,
          wrong: this.wrong,
        };
        const res = await TriviaAPI.createTriviaScore(this.triviaId, data);
        this.scoreDetails = res;
        this.scoreDialog = true;
      }
    },
  },
  created() {
    if (this.triviaId !== null) this.getTrivia(this.triviaId);
  },
  computed: {
    ...mapGetters({
      authUser: "auth/user",
    }),
  },
  methods: {
    async getTrivia(id) {
      const res = (await TriviaAPI.getTriviaItem(id)).trivia;
      this.trivia = res;
    },
    startTrivia() {
      this.end = false;
      this.start = false;
      this.correct = 0;
      this.wrong = 0;
      this.scoreDialog = false;
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
    updatePrev() {
      if (this.next == 0) return;
      this.next--;
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
