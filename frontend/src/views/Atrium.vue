<template>
  <div id="site-logo-container">
    <router-link to="/games">
      <img id="site-logo" src="@/assets/labyrinth.png" />
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'Atrium',
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
