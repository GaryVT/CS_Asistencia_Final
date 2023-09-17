<template>
  <div>
    <v-btn icon color="primary" dark @click="editItem2">
      <v-icon>mdi-pencil</v-icon>
    </v-btn>
    <v-btn icon color="error" dark @click="deleteItem2">
      <v-icon>mdi-delete</v-icon>
    </v-btn>
  </div>
</template>

<script>
export default {
  methods: {
    editItem2() {
      // Lógica para editar el elemento
      console.log("xxx")
    },
    deleteItem2() {
      // Lógica para eliminar el elemento
    }
  }
};
</script>