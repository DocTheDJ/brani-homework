<script setup lang="ts">
  import TagList from './components/TagList.vue'
  import DataTable from './components/DataTable.vue'
</script>

<!-- wrapper app for TagList and DataTable -->
<template>
  <v-container>
    <v-row>
      <v-col>
        <TagList/>
        <DataTable/>
      </v-col>
    </v-row>
  </v-container>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

.v-container {
  max-width: 100%;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    /* padding-right: calc(var(--section-gap) / 2); */
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
