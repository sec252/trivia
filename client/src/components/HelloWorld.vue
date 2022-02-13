<template lang="pug">
  v-container
    v-row.text-center
      v-col(cols=6)
        TriviaCreatePool(@new="addTrivia")
      v-col(cols=6)
        UserCreateForm(@new="addUser")
      v-col(cols=6)
        h1 Trivia Pools
        div(v-for="trivia in triviaPools")
          p(:key="trivia.id") {{trivia.id}}) {{trivia.name}}
      v-col(cols=6)
        h1 Users
        v-row(v-for="user in users")
          p(:key="user.id") {{user.id}}) {{user.username}}
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



</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  components: {
    TriviaCreatePool: () => import("./TriviaCreatePool.vue"),
    UserCreateForm: () => import("./UserCreateForm.vue"),
    UserDetailsDialog: () => import("./UserDetailsDialog.vue"),
    UserEditFormDialog: () => import("./UserEditFormDialog.vue"),
  },
  data: () => ({
    detailsDialog: false,
    editDialog: false,
    users: [],
    user: {},
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
    async editUser(id) {
      this.user = (
        await axios.get(`http://localhost:5000/api/users/${id}`)
      ).data?.user;
      this.editDialog = true;
    },
    updateUser(user) {
      this.users.forEach((u) => {
        if (u.id == user.id) {
          u.username = user.username;
          u.active = user.active;
        }
      });
    },
    async deleteUser(id) {
      await axios.delete(`http://localhost:5000/api/users/${id}`);
      this.users = this.users.filter((u) => u.id !== id);
    },
  },
};
</script>
