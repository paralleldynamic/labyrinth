<template>
  <sidebar :show="show" @toggleSidebar="toggleSidebar">
    <div class="sidebar-content">
      <h1>{{ game.title }}</h1>
      <p>{{ game.tagline }}</p>
      <button @click="submitDelete">Delete This Game</button>
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
.sidebar-content {
  display: grid;
  width: 100%;
  margin: 1em;
}

.sidebar-content h1 {
  justify-self: center;
}

.sidebar-content p {
  justify-self: center;
}

.sidebar-content button {
  width: 80%;
  justify-self: center;
  text-align: center;
}
</style>
