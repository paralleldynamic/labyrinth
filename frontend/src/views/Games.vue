<template>
  <div class='page-wrapper'>
    <div class="card-container">
      <ContentCard />
    </div>
  </div>
</template>

<script>
import ContentCard from '@/components/ContentCard.vue';

export default {
  name: 'Games',
  components: {
    ContentCard,
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
