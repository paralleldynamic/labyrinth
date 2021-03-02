<template>
  <sidebar :show="show" @toggleSidebar="toggleSidebar">
    <div class="sidebar-content">
      <img id="sidebar-image" v-bind:src="game.logo_img_src"
           v-bind:alt="game.logo_img_alt"
           v-bind:style="game.logo_img_style">
      <h1 id="sidebar-title">{{ game.title }}</h1>
      <p id="sidebar-description">{{ game.tagline }}</p>
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
      // const { id } = this.game;
      // const { accessToken } = this.$store.state.auth;
      // await this.deleteGame({ id, accessToken })
      //   .then(this.toggleSidebar(this.game))
      //   .catch((error) => error);
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

.sidebar-content > h1 {
  justify-self: center;
}

.sidebar-content > p {
  justify-self: center;
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
