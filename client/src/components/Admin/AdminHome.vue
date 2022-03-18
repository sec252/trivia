<template lang="pug">
  v-container
    v-row
      v-col(cols=6)
        TriviaCreatePool(@new="addTrivia")
      v-col(cols=6)
        v-card()
          v-card-title.text-h5 Username: 
            strong.ml-2 {{authUser.username}}
          v-card-text.pt-4
            p(v-if="authUser.active").green--text Active User
            p(v-else).red--text This user is not active
            p Plays: 132
          v-divider
          v-card-actions
            v-spacer
            v-btn(text)
              | Role: {{authUser.role}}
      AdminTriviaTable(:key="rerender")
      AdminUsersTable
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "AdminHome",
  components: {
    TriviaCreatePool: () => import("../Trivia/TriviaCreatePool.vue"),
    AdminTriviaTable: () => import("./AdminTriviaTable.vue"),
    AdminUsersTable: () => import("./AdminUsersTable.vue"),
  },
  data: () => ({
    rerender: 1,
  }),
  computed: {
    ...mapGetters({
      authUser: "auth/user",
      isAuth: "auth/isLoggedIn",
    }),
  },
  methods: {
    addTrivia() {
      this.rerender++;
    },
  },
};
</script>
