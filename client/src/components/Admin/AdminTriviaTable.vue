<template lang="pug">
v-col(:cols="authUser.role =='admin' ? 6 : 12").text-center: v-card(flat)
        v-row(no-gutters).px-2
            h2.py-2 Trivia Pools
            v-spacer
            h2.py-2 Total: ({{triviaPools.length}})
        v-data-table(
            :headers="headers"
            fixed-header
            :items="triviaPools"
            height="300"
            hide-default-footer
            
        )
            template(v-slot:item.actions='{ item }')
                v-btn(icon small color="error" @click="deleteTrivia(item.id)").mr-2
                    v-icon mdi-delete
                v-btn(icon small color="info"  @click="editTriviaPool(item.id)")
                    v-icon mdi-pencil
                
        TriviaEditFormDialog(:dialog="editTriviaDialog" :triviaPool="triviaPool" @cancel="editTriviaDialog=false", @updateTrivia="updateTriviaPool")
</template>

<script>
import { TriviaAPI } from "../../services/trivia";
import { mapGetters } from "vuex";
export default {
  name: "AdminTriviaTable",
  components: {
    TriviaEditFormDialog: () => import("../Trivia/TriviaEditFormDialog.vue"),
  },
  data: () => ({
    triviaPools: [],
    headers: [
      {
        text: "Title",
        align: "start",
        value: "name",
      },
      { text: "Category", value: "category" },
      { text: "Plays", value: "plays" },
      { text: "Actions", value: "actions", sortable: false, align: "end" },
    ],
    editTriviaDialog: false,
    triviaPool: {},
  }),
  computed: {
    ...mapGetters({
      authUser: "auth/user",
      isAuth: "auth/isLoggedIn",
    }),
  },
  async created() {
    this.triviaPools = (await TriviaAPI.getTriviaUserCollection()).body;
  },
  methods: {
    async editTriviaPool(id) {
      try {
        this.triviaPool = (await TriviaAPI.getTriviaItem(id)).trivia;
        this.editTriviaDialog = true;
      } catch (error) {
        console.error(error.response.data);
      }
    },
    async deleteTrivia(id) {
      await TriviaAPI.deleteTriviaItem(id);
      this.triviaPools = this.triviaPools.filter((t) => t.id !== id);
    },
    updateTriviaPool(triviaPool) {
      this.triviaPools.forEach((t) => {
        if (t.id == triviaPool.id) {
          t.name = triviaPool.name;
        }
      });
    },
  },
};
</script>
