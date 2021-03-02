<template>
  <sidebar :show="show" @toggleSidebar="toggleSidebar">
    <div class="game-detail-sidebar">
      <div class="sidebar-header">
        <img id="sidebar-image" v-bind:src="game.logo_img_src"
            v-bind:alt="game.logo_img_alt"
            v-bind:style="game.logo_img_style">
        <h1 id="sidebar-title">{{ game.title }}</h1>
      </div>
      <div class="sidebar-content">
        <p id="sidebar-description">{{ game.tagline }}</p>
      </div>
      <div class="sidebar-footer">
        <button @click="submitDelete" v-if="false">Delete This Game</button>
      </div>
    </div>
  </sidebar>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue';
import { mapActions } from 'vuex';

export default {
  name: 'GameDetailSidebar',
  components: {
    Sidebar,
  },
  props: [
    'show',
    'game',
  ],
  emit: [
    'toggleSidebar',
  ],
  methods: {
    ...mapActions(['deleteGame']),
    toggleSidebar(game) {
      this.$emit('toggleSidebar', game);
    },
    async submitDelete() {
      const { id } = this.game;
      const { accessToken } = this.$store.state.auth;
      await this.deleteGame({ id, accessToken })
        .then(this.toggleSidebar(this.game))
        .catch((error) => error);
    },
  },
};
</script>

<style scoped>
.game-detail-sidebar {
  width: 100%;
  margin: 1em;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(10, 1fr);
}

.sidebar-header {
  grid-area: 1 / 1 / 2 / 6;
}

.sidebar-content {
  grid-area: 2 / 1 / 9 / 6;
}

.sidebar-footer {
  grid-area: 9 / 1 / 11 / 6;
}

.sidebar-content > button {
  width: 80%;
  justify-self: center;
  text-align: center;
}

#sidebar-image {
  max-width: 100%;
  max-height: 100%;
}
</style>
