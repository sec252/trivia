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
      v-col(:cols="authUser.role =='admin' ? 6 : 12").text-center: v-card(flat)
        h1.py-2 Trivia Pools
        v-row( no-gutters v-for="trivia in triviaPools" :key="trivia.name").px-3
          p {{trivia.id}}) {{trivia.name}} - ({{trivia.category}})
          v-spacer
          v-btn(icon color="error" @click="deleteTrivia(trivia.id)").mr-2
            v-icon mdi-delete
          v-tooltip(bottom)
            template(v-slot:activator='{ on, attrs }')
              v-icon(color='info' dark v-bind='attrs' v-on='on'
              @click="editTriviaPool(trivia.id)").mr-2
                | mdi-pencil
            span Edit Trivia Pool
      v-col(cols=6 v-if="authUser.role =='admin'").text-center: v-card(flat)
        h1.py-2 Users
        v-row(no-gutters v-for="user in users" :key="user.name").px-3
          p {{user.id}}) {{user.username}}
          v-spacer
          v-btn(icon color="error"  @click="deleteUser(user.id)").mr-2
            v-icon mdi-delete
          v-tooltip(bottom)
            template(v-slot:activator='{ on, attrs }')
              v-icon(color='info' dark v-bind='attrs' v-on='on'
              @click="editUser(user.id)").mr-2
                | mdi-pencil
            span Edit User
          v-tooltip(bottom)
            template(v-slot:activator='{ on, attrs }')
              v-icon(color='primary' dark v-bind='attrs' v-on='on'
              @click="getUser(user.id)").mr-2
                | mdi-account
            span Get User Details

    UserDetailsDialog(:dialog="detailsDialog", :user="user" @cancel="detailsDialog=false")
    UserEditFormDialog(:dialog="editDialog", :user="user" @cancel="editDialog=false" @update="updateUser")
    TriviaEditFormDialog(:dialog="editTriviaDialog" :triviaPool="triviaPool" @cancel="editTriviaDialog=false", @updateTrivia="updateTriviaPool")



</template>

<script>
import { UsersAPI } from "../services/users";
import { TriviaAPI } from "../services/trivia";
import { mapGetters } from "vuex";
export default {
  name: "AdminHome",
  components: {
    TriviaCreatePool: () => import("./Trivia/TriviaCreatePool.vue"),
    UserCreateForm: () => import("./UserCreateForm.vue"),
    UserDetailsDialog: () => import("./UserDetailsDialog.vue"),
    UserEditFormDialog: () => import("./UserEditFormDialog.vue"),
    TriviaEditFormDialog: () => import("./Trivia/TriviaEditFormDialog.vue"),
  },
  data: () => ({
    detailsDialog: false,
    triviaDetailsDialog: false,
    editDialog: false,
    editTriviaDialog: false,
    users: [],
    user: {},
    triviaPool: {},
    triviaPools: [],
  }),
  async created() {
    this.users = (await UsersAPI.getUserCollection()).users;

    this.triviaPools = (await TriviaAPI.getTriviaUserCollection()).body;
  },
  computed: {
    ...mapGetters({
      authUser: "auth/user",
      isAuth: "auth/isLoggedIn",
    }),
  },
  methods: {
    addUser(user) {
      this.users.push(user);
    },
    addTrivia(trivia) {
      this.triviaPools.push(trivia);
    },
    async getUser(id) {
      const user = (await UsersAPI.getUserItem(id)).user;
      this.user = user;
      this.detailsDialog = true;
    },
    async getTrivia(id) {
      const trivia = (await TriviaAPI.getTriviaItem(id)).trivia;
      this.triviaPool = trivia;
      this.triviaDetailsDialog = true;
    },
    async editUser(id) {
      this.user = (await UsersAPI.getUserItem(id)).user;
      this.editDialog = true;
    },
    async editTriviaPool(id) {
      try {
        this.triviaPool = (await TriviaAPI.getTriviaItem(id)).trivia;
        this.editTriviaDialog = true;
      } catch (error) {
        console.error(error.response.data);
      }
    },
    updateUser(user) {
      this.users.forEach((u) => {
        if (u.id == user.id) {
          u.username = user.username;
          u.active = user.active;
        }
      });
    },
    updateTriviaPool(triviaPool) {
      this.triviaPools.forEach((t) => {
        if (t.id == triviaPool.id) {
          t.name = triviaPool.name;
        }
      });
    },
    async deleteUser(id) {
      await UsersAPI.deleteUserItem(id);
      this.users = this.users.filter((u) => u.id !== id);
    },
    async deleteTrivia(id) {
      await TriviaAPI.deleteTriviaItem(id);
      this.triviaPools = this.triviaPools.filter((t) => t.id !== id);
    },
  },
};
</script>
