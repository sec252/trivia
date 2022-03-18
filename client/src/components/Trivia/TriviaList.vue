<template lang="pug">
  v-row(dense no-gutters)
    v-col(v-for="trivia in trivias" cols=12 md=6 :key="trivia.id").pa-2
      TriviaCard(
        :trivia="trivia"
        @play="playTrivia"
      )
    TriviaCardPlay(
      :triviaId="this.triviaId" 
      :dialog="dialog"
      :key="dialog"
      @cancel="dialog=false"
    )
</template>

<script>
import { TriviaAPI } from "../../services/trivia";
import { mapGetters } from "vuex";
export default {
  name: "TriviaList",
  components: {
    TriviaCard: () => import("./TriviaCard.vue"),
    TriviaCardPlay: () => import("./TriviaCardPlay.vue"),
  },
  props: {
    trivias: {
      type: Array,
      required: true,
      default: () => [],
    },
  },
  data: () => ({
    triviaId: null,
    dialog: false,
  }),
  computed: {
    ...mapGetters({
      authUser: "auth/user",
    }),
  },
  methods: {
    async playTrivia(id) {
      let userId;
      if (this.authUser.id == undefined) {
        userId = 0;
      } else {
        userId = this.authUser.id;
      }
      const res = await TriviaAPI.updateTriviaPlays(id, { userId: userId });
      this.trivias.forEach((element) => {
        if (element.id == id) {
          element.plays = res.plays;
        }
      });
      this.triviaId = id;
      this.dialog = true;
    },
  },
};
</script>
