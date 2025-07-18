
<script setup lang="ts">
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
import ImageUpload from './components/ImageUpload.vue'
</script>

<template>
  <AppHeader />
  <!-- <main>
    <ImageUpload />
  </main> -->
  <AppFooter />
</template>


<style scoped>
main {
  min-height: 70vh;
  background: #f1f5f9;
  padding: 2rem 0 0 0;
}
</style>
