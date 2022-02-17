<template lang="pug">
  v-container
    v-row.text-center
      v-col(cols=6)
        TriviaCreatePool(@new="addTrivia")
      v-col(cols=6)
        UserCreateForm(@new="addUser")
      v-col(cols=6): v-card
        h1 Trivia Pools
        v-row( no-gutters v-for="trivia in triviaPools" :key="trivia.name").px-3
          p {{trivia.id}}) {{trivia.name}}
          v-spacer
          v-btn(icon color="error" @click="deleteTrivia(triviaPool.id)").mr-2
            v-icon mdi-delete
          v-tooltip(bottom)
            template(v-slot:activator='{ on, attrs }')
              v-icon(color='info' dark v-bind='attrs' v-on='on'
              @click="editTriviaPool(trivia.id)").mr-2
                | mdi-pencil
            span Edit Trivia Pool
          v-tooltip(bottom)
            template(v-slot:activator='{ on, attrs }')
              v-icon(color='primary' dark v-bind='attrs' v-on='on'
              @click="getTrivia(trivia.id)").mr-2
                | mdi-clipboard-list-outline
            span Get Trivia Details
      v-col(cols=6): v-card
        h1 Users
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
    TriviaDetailDialog(:dialog="triviaDetailsDialog" :trivia="triviaPool" @cancel="triviaDetailsDialog=false")



</template>

<script>
import axios from "axios";
import TriviaDetailDialog from "./TriviaDetailDialog.vue";
export default {
  name: "HelloWorld",
  components: {
    TriviaCreatePool: () => import("./TriviaCreatePool.vue"),
    UserCreateForm: () => import("./UserCreateForm.vue"),
    UserDetailsDialog: () => import("./UserDetailsDialog.vue"),
    UserEditFormDialog: () => import("./UserEditFormDialog.vue"),
    TriviaEditFormDialog: () => import("./TriviaEditFormDialog.vue"),
    TriviaDetailDialog,
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
    const users = await axios.get("http://localhost:5000/api/users/");

    this.users = users.data?.users;

    const trivias = await axios.get("http://localhost:5000/api/trivias/");
    this.triviaPools = trivias.data?.body;
  },
  methods: {
    async post() {
      const user = { username: "asdadsa" };
      await axios.post("http://localhost:5000/api/users/", user);
    },
    addUser(user) {
      this.users.push(user);
    },
    addTrivia(trivia) {
      this.triviaPools.push(trivia);
    },
    async getUser(id) {
      const user = (await axios.get(`http://localhost:5000/api/users/${id}`))
        .data?.user;
      this.user = user;
      this.detailsDialog = true;
    },
    async getTrivia(id) {
      const trivia = (
        await axios.get(`http://localhost:5000/api/trivias/${id}`)
      ).data?.trivia;
      this.triviaPool = trivia;
      this.triviaDetailsDialog = true;
    },
    async editUser(id) {
      this.user = (
        await axios.get(`http://localhost:5000/api/users/${id}`)
      ).data?.user;
      this.editDialog = true;
    },
    async editTriviaPool(id) {
      this.triviaPool = (
        await axios.get(`http://localhost:5000/api/trivias/${id}`)
      ).data?.trivia;
      this.editTriviaDialog = true;
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
      await axios.delete(`http://localhost:5000/api/users/${id}`);
      this.users = this.users.filter((u) => u.id !== id);
    },
    async deleteTrivia(id) {
      await axios.delete(`http://localhost:5000/api/trivias/${id}`);
      this.triviaPools = this.triviaPools.filter((t) => t.id !== id);
    },
  },
};
</script>
