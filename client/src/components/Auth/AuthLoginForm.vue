<template lang="pug">
  v-card-text.px-4
    v-form(ref='loginForm' v-model='valid' lazy-validation)
      v-row
        v-col(cols='12')
          v-text-field(
            color="default" v-model='username' 
            :rules="[rules.required, rules.min, rules.username]" 
            label='Username' 
            required
          )
        v-col(cols='12')
          v-text-field(
            color="default" v-model='password' 
            :append-icon="show1?'eye':'eye-off'" :rules='[rules.required, rules.min]' :type="show1 ? 'text' : 'password'" 
            label='Password' 
            hint='At least 4 characters' 
            counter 
            @click:append='show1 = !show1'
          )
        v-col(cols='12')
          v-alert(type="error" v-if="invalidCredentials") {{errorMsg}}
          v-row.pa-2
            v-spacer
            v-btn(
              large 
              color='error' 
              @click='$emit("close")'
            ).mr-2  cancel 
            v-btn(
              large 
              :disabled='!valid' 
              color='primary' 
              @click='validate'
            )  {{submitButton}}

</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  name: "AuthLoginForm",
  props: {
    register: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  data: () => ({
    invalidCredentials: false,
    errorMsg: "Invalid Credentials",
    password: "",
    username: "",
    rules: {
      required: (value) => !!value || "Required.",
      min: (v) => (v && v.length >= 4) || "Min 4 characters",
      username: (v) => /^[A-Za-z][A-Za-z0-9_]{4,29}$/.test(v) || "No spaces",
    },
    show1: false,
    valid: true,
  }),
  computed: {
    ...mapGetters({
      authUser: "auth/user",
      isAuth: "auth/isLoggedIn",
    }),
    submitButton() {
      if (this.register) return "Register";
      return "Login";
    },
  },
  methods: {
    ...mapActions({
      loginUser: "auth/loginUser",
      registerUser: "auth/registerUser",
      addNotification: "notifications/addNotification",
    }),
    async validate() {
      if (this.$refs.loginForm.validate()) {
        // submit form to server/API here...
        if (!this.register) {
          await this.login();
        } else {
          await this.signup();
        }
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
    async login() {
      const user = {
        username: this.username,
        password: this.password,
      };
      await this.loginUser(user).then(() => {
        if (this.isAuth) {
          this.$router.push("/admin");
          this.$emit("close");
        } else {
          // Handle error
          this.handleError();
        }
      });
    },
    async signup() {
      try {
        const user = {
          username: this.username,
          password: this.password,
        };
        await this.registerUser(user).then(() => {
          if (this.isAuth) {
            this.$router.push("/admin");
            this.$emit("close");
          }
        });
      } catch (error) {
        const msg = error.response?.data?.message;
        this.handleError(msg);
      }
    },
    handleError(msg) {
      this.username = "";
      this.password = "";
      this.errorMsg = msg;
      this.invalidCredentials = true;
      setTimeout(() => {
        this.invalidCredentials = false;
      }, 5000);
    },
  },
};
</script>

<style></style>
