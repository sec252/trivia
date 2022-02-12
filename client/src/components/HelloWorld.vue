<template lang="pug">
  v-container
    v-row.text-center
      v-col: h1 Hello world

      v-col: div(v-for="user in users")
        p(:key="user.id") {{user.id}}) {{user.username}}
        



</template>

<script>
import axios from "axios";
export default {
  name: "HelloWorld",

  data: () => ({
    users: [],
  }),
  async created() {
    const res = await axios.get("http://localhost:5000/api/users");
    this.users = res.data;
  },
};
</script>
