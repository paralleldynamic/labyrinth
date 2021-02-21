<template>
  <div id="site-logo-container">
    <router-link to="/games">
      <img id="site-logo" src="@/assets/labyrinth.png" />
    </router-link>
  </div>
</template>

<script>
import { mapActions } from 'vuex';

export default {
  name: 'Atrium',
  // eslint-disable-next-line
  methods: {
    ...mapActions(['logout']),
  },
  created() {
    this.logout();
  },
};
</script>

<style scoped>
#site-logo {
  width: 20rem;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
