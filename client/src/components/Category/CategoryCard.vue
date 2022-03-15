<template lang="pug">
v-card.mx-auto( )
  v-toolbar(
    :elevation="1"

  ).mb-2 
    v-icon.mr-3 mdi-shape-plus
    v-toolbar-title {{category.name}}
    v-spacer
    v-tooltip(bottom)
      template( v-slot:activator="{ on, attrs }")
        v-btn(
          fab 
          x-small 
          color="success" 
          @click="$emit('new', category.id)" 
          v-bind="attrs"
          v-on="on"
        )
          v-icon mdi-plus
      span Add New Trivia
  v-card-text.text-h5.font-weight-bold
    v-data-table(
    height=200
    dense
    :headers="headers"
    :items="trivias"
    item-key="name"
    :page.sync="page"
    :items-per-page="itemsPerPage"
    hide-default-footer
    @page-count="pageCount = $event"
    class="elevation-0"
    )
      template(v-slot:item.actions="{ item }")
        v-btn(icon small color='primary')
          v-icon mdi-play
    .text-center.pt-2
      v-pagination(
        circle
        v-model="page"
        :length="pageCount"
        :total-visible="7"
      )

</template>

<script>
import { TriviaAPI } from "../../services/trivia";

export default {
  name: "CatergoryCard",
  props: {
    category: {
      type: Object,
      required: true,
    },
  },
  data: () => ({
    page: 1,
    pageCount: 0,
    itemsPerPage: 5,
    headers: [
      {
        text: "Trivia",
        value: "name",
      },
      {
        text: "Total Plays",
        value: "plays",
        align: "end",
      },
      {
        text: "",
        value: "actions",
        align: "end",
        width: "10px",
      },
    ],
    trivias: [{ id: 1, name: "Javascript" }],
  }),
  created() {
    this.getTrivias(this.category.id);
  },
  methods: {
    async getTrivias(id) {
      this.trivias = (await TriviaAPI.getTriviaCategoryCollection(id)).body;
    },
  },
};
</script>
