<template>
  <div id="app">
    <table class="table">
      <thead>
        <th>Data</th>
        <th>Informações</th>
        <th>Árvore</th>
        <th>Espécie</th>
        <th>Grupo de árvores</th>
        <th>Peso bruto</th>
      </thead>
      <tbody>
        <tr v-for="harvest in harvests" :key="harvest.id">
          <td>{{ harvest.harvest_date }}</td>
          <td>{{ harvest.info }}</td>
          <td v-if="harvest.tree === null">{{ harvest.tree }}</td>
          <td v-else>{{ harvest.tree.description }}</td>
          <td v-if="harvest.tree === null">{{ harvest.tree }}</td>
          <td v-else-if="harvest.tree.specie === null">{{ harvest.tree.specie }}</td>
          <td v-else>{{ harvest.tree.specie.description }}</td>
          <td v-if="harvest.tree_group === null">{{ harvest.tree_group }}</td>
          <td v-else>{{ harvest.tree_group.name }}</td>
          <td>{{ harvest.gross_weight }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      harvests: []
    }
  },
  async created() {
    var response = await fetch('http://localhost:8000/api/harvest/');
    this.harvests = await response.json();
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
