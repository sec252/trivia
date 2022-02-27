<template lang="pug">
div
  v-app-bar( dense)
    v-toolbar-title#title Trivia App
    v-spacer
    v-btn(text to="/admin") Secret Page
    v-btn(text to="/about") About
    v-btn(text to="/") Trivias
    v-btn(text) Catagories
    v-menu(left bottom)
      template(v-slot:activator='{ on, attrs }')
        v-btn(icon v-bind='attrs' v-on='on')
          v-icon mdi-cog
      v-list
        v-list-item-group(
          v-model="selectedItem"
          color="primary"
        )
          v-list-item(v-for='(item, i) in menu' :key='i')
            v-list-item-icon
              v-icon {{item.icon}}
            v-list-item-content
              v-list-item-title(v-text='item.title')



</template>

<script>
export default {
  name: "TheNavBar",
  data: () => ({
    selectedItem: 1,
    menu: [
      { icon: "mdi-account-plus", title: "Register" },
      { icon: "mdi-login", title: "Login" },
      { icon: "mdi-logout", title: "Logout" },
      { icon: "mdi-account-details", title: "Account Details" },
    ],
  }),
  methods: {
    menuItems() {
      return this.menu;
    },
    toHome() {
      this.$router.push("/");
    },
  },
};
</script>

<style scoped>
#title {
  cursor: pointer;
}
</style>
