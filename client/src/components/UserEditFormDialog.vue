<template lang="pug">
.text-center
  v-dialog(v-model='dialog' width='500')
    v-card
      v-card-title.text-h5.grey.lighten-2
        | {{user.username}}
      v-card-text
       v-text-field(v-model="user.username", label="Username")
       v-checkbox(
         v-model="user.active",
         :label="user.active ? 'Active' : 'Deactivated'"
        )

       
      v-divider
      v-card-actions
        v-spacer
        v-btn(color='error' text @click='$emit("cancel")')
          | Cancel
        v-btn(color='primary' text @click='save(user.id)')
          | Save

</template>

<script>
import { UsersAPI } from "../services/users";
export default {
  name: "UserEditFormDialog",
  props: {
    dialog: {
      type: Boolean,
    },
    user: {
      type: Object,
    },
  },
  methods: {
    async save(id) {
      const user = {
        username: this.user.username,
        active: this.user.active,
      };

      const editedUser = (await UsersAPI.editUserItem(id, user)).user;

      this.$emit("update", editedUser);
      this.$emit("cancel");
    },
  },
};
</script>
