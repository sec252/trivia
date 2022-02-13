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
        div(v-for="user in users")
          p(:key="user.id") {{user.id}}) {{user.username}}




</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",
  components: {
    TriviaCreatePool: () => import("./TriviaCreatePool.vue"),
    UserCreateForm: () => import("./UserCreateForm.vue"),
  },
  data: () => ({
    users: [],
    triviaPools: [],
  }),
  async created() {
    const users = await axios.get("http://localhost:5000/api/users/");
    console.log(users);
    this.users = users.data?.users;

    const trivias = await axios.get("http://localhost:5000/api/trivias/");
    console.log(trivias);
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
  },
};
</script>
