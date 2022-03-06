<template lang="pug">
v-card 
  v-card-text
    v-text-field(
      v-model="username",
      label="Username",
      required
    )
    v-text-field(
      v-model="password",
      label="Password",
      type="password"
      required
    )
  v-divider
  v-card-actions
    v-spacer
    v-btn(
      text 
      @click="createUser"
      :disabled="authUser.role != 'admin'"  
    ) {{authUser.role != 'admin' ? 'Not Authorized' : 'Create User Test'}}

        



</template>

<script>
import { UsersAPI } from "../services/users";
import { mapGetters } from "vuex";
export default {
  name: "UserCreateForm",
  data: () => ({
    username: "",
    password: "",
  }),
  computed: {
    ...mapGetters({
      authUser: "auth/user",
      isAuth: "auth/isLoggedIn",
    }),
  },
  methods: {
    async createUser() {
      const user = {
        username: this.username,
        password: this.password,
      };
      const newUser = (await UsersAPI.createUser(user)).user;

      this.username = "";
      this.password = "";
      this.$emit("new", newUser);
    },
  },
};
</script>
