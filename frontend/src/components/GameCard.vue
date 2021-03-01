<template>
  <content-card @click="cardClicked()">
    <template v-slot:card-image>
      <img v-bind:src="game.logo_img_src"
           v-bind:alt="game.logo_img_alt"
           v-bind:style="game.logo_img_style">
    </template>
    <template v-slot:card-title>
      <h2>{{ game.title }}</h2>
    </template>
    <template v-slot:card-description>
      <p>{{ game.tagline }}</p>
    </template>
  </content-card>
</template>

<script>
import ContentCard from '@/components/ContentCard.vue';

export default {
  name: 'GameCard',
  components: {
    ContentCard,
  },
  props: [
    'game',
  ],
  emits: [
    'cardClicked',
  ],
  methods: {
    cardClicked() {
      this.$emit('cardClicked', this.game);
    },
  },
};
</script>
