<template lang="pug">
v-card 
  v-card-text
    v-text-field(
      v-model="username",
      label="Username",
      required
    )
  v-divider
  v-card-actions
    v-spacer
    v-btn(text @click="createUser") Create User Test

        



</template>

<script>
import axios from "axios";
export default {
  name: "UserCreateForm",

  data: () => ({
    username: "",
  }),
  methods: {
    async createUser() {
      const user = { username: this.username };
      const newUser = (
        await axios.post("http://localhost:5000/api/users/", user)
      ).data?.user;

      this.username = "";
      this.$emit("new", newUser);
    },
  },
};
</script>
