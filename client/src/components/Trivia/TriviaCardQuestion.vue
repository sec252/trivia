<template lang="pug">
v-expand-transition
  v-card.mx-auto(:color='color' dark minHeight="180px" width='500px')
    v-card-title
      span.text-h6.font-weight-light {{number + 1}}/{{total}}
    v-card-text.text-h5.font-weight-bold.white--text
      | {{show ? answer : text}}
      v-text-field(
        autofocus
        v-model="response"
        placeholder="Type Answer"
        @keydown.enter="onEnter"
        hint="Press Enter to Submit Answer"
        :hint-persistant="response !=''"
      ).mt-2
    v-card-actions
      v-row( no-gutters).mb-2
        v-spacer
        //- v-btn(outlined color="white" @click="$emit('prev'); show=false; color='info';" v-if="number>0").mr-2 Previous
        v-btn(outlined color="white" @click="next" v-if="show").mr-2 Next

</template>

<script>
import { TriviaAPI } from "../../services/trivia";
import { mapActions } from "vuex";
export default {
  name: "TriviaCardQuestion",
  props: {
    number: {
      type: Number,
      required: true,
      default: 1,
    },
    id: {
      type: Number,
      required: true,
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
    response: "",
    color: "info",
  }),
  methods: {
    ...mapActions({
      addNotification: "notifications/addNotification",
    }),
    async onEnter() {
      try {
        if (this.color != "info") {
          this.next();
          return;
        }
        const data = {
          response: this.response,
        };
        const res = await TriviaAPI.answerTrivia(this.id, data);
        this.getColor(res.isCorrect);
        let msg = res.isCorrect
          ? "Correct!"
          : "Wrong! Go Fucking Kill Yourself!";
        let color = res.isCorrect ? "success" : "error";
        this.addNotification({
          message: msg,
          type: color,
        });
      } catch (error) {
        this.addNotification({
          message: error.response.data.message,
          type: "error",
        });
      }
    },
    next() {
      this.show = false;
      this.color = "info";
      this.response = "";
      this.$emit("next");
    },
    getColor(isCorrect) {
      isCorrect ? (this.color = "success") : (this.color = "error");
      this.show = !this.show;
      isCorrect ? this.$emit("addCorrect") : this.$emit("addWrong");
    },
  },
};
</script>
