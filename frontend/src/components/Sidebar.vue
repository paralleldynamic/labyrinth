<template>
  <transition name="slide">
    <div v-if="show"
          class="sidebar-panel">
          <h3>Test Title lol</h3>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Sidebar',
  props: [
    'show',
  ],
  methods: {
  },
};
</script>

<style scoped>
.sidebar-panel {
  width: 50vw;
  height: 100vh;
  border: 3px solid #191919;
}
</style>
