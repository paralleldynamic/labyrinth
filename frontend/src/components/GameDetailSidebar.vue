<template>
  <sidebar :show="show" @toggleSidebar="toggleSidebar">
    <div class="sidebar-content">
      <h1>{{ card.title }}</h1>
      <p>{{ card.tagline }}</p>
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
    'card',
  ],
  emit: [
    'toggleSidebar',
  ],
  methods: {
    ...mapActions(['deleteGame']),
    toggleSidebar() {
      this.$emit('toggleSidebar');
    },
    submitDelete() {
      const { id } = this.card;
      const { accessToken } = this.$store.state.auth;
      this.deleteGame({ id, accessToken });
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
