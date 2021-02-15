<template>
  <div class='page-wrapper'>
    <div class="card-container">
      <ContentCards />
    </div>
  </div>
</template>

<script>
import ContentCards from '@/components/ContentCards.vue';

export default {
  name: 'Games',
  components: {
    ContentCards,
  },
};
</script>

<style scoped>
.card-container {
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  flex-wrap: wrap;
  grid-template-columns: repeat(autofill, 1fr);
  grid-auto-rows: auto;
}
</style>
