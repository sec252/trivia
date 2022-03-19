<template lang="pug">
v-col(:cols="authUser.role =='admin' ? 4 : 12").text-center: v-card(flat)
        v-row(no-gutters).px-2
            h2.py-2 Users
            v-spacer
            h2.py-2 Total: ({{users.length}})
        v-data-table(
            :headers="headers"
            fixed-header
            :items="users"
            height="300"
            hide-default-footer
            disable-pagination
            
        )
            template(v-slot:item.actions='{ item }')
                v-btn(icon small color="error" @click="deleteUser(item.id)").mr-2
                    v-icon mdi-delete
                v-btn(icon small color="info"  @click="editUser(item.id)")
                    v-icon mdi-pencil
                v-btn(icon small color="primary"  @click="getUser(item.id)")
                    v-icon mdi-account
        UserDetailsDialog(:dialog="detailsDialog", :user="user" @cancel="detailsDialog=false")      
        UserEditFormDialog(:dialog="editDialog", :user="user" @cancel="editDialog=false" @update="updateUser")
</template>

<script>
import { UsersAPI } from "../../services/users";
import { mapGetters } from "vuex";
export default {
  name: "AdminUsersTable",
  components: {
    UserDetailsDialog: () => import("../UserDetailsDialog.vue"),
    UserEditFormDialog: () => import("../UserEditFormDialog.vue"),
  },
  data: () => ({
    detailsDialog: false,
    editDialog: false,
    users: [],
    user: {},
    headers: [
      {
        text: "Username",
        align: "start",
        value: "username",
      },
      {
        text: "Actions",
        value: "actions",
        sortable: false,
        align: "end",
      },
    ],
  }),
  computed: {
    ...mapGetters({
      authUser: "auth/user",
      isAuth: "auth/isLoggedIn",
    }),
  },
  async created() {
    this.users = (await UsersAPI.getUserCollection()).users;
  },
  methods: {
    addUser(user) {
      this.users.push(user);
    },
    addTrivia() {
      this.rerender++;
    },
    async getUser(id) {
      const user = (await UsersAPI.getUserItem(id)).user;
      this.user = user;
      this.detailsDialog = true;
    },
    async editUser(id) {
      this.user = (await UsersAPI.getUserItem(id)).user;
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
      await UsersAPI.deleteUserItem(id);
      this.users = this.users.filter((u) => u.id !== id);
    },
  },
};
</script>
