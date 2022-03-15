<template lang="pug">
v-dialog(
  transition="dialog-bottom-transition"
  max-width="600"
  v-model="dialog"
)
  v-card(
    flat
    tile
  )
    v-toolbar(
      :elevation="1"
      color="primary"
      dark
    ).mb-2 
      v-icon.mr-3 {{icon}}
      v-toolbar-title {{title}}
      v-spacer
      v-btn(icon @click="$emit('cancel')")
        v-icon mdi-close

    AuthLoginForm(
      @close="$emit('cancel')"
      :register="register"
    )

</template>

<script>
import AuthLoginForm from "./AuthLoginForm.vue";
export default {
  name: "AuthDialog",
  components: {
    AuthLoginForm,
  },
  props: {
    dialog: {
      type: Boolean,
      required: true,
    },
    register: {
      type: Boolean,
      required: false,
      default: false,
    },
  },
  computed: {
    title() {
      if (this.register) return "Register";
      return "Login";
    },
    icon() {
      if (this.register) return "mdi-account-plus";
      return "mdi-login";
    },
  },
};
</script>
