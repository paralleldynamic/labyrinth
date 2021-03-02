<template>
  <transition name="slide">
    <div @click.stop
         v-if="show"
         class="sidebar-panel">
      <slot />
    </div>
  </transition>
</template>

<script>
export default {
  name: 'Sidebar',
  props: [
    'show',
  ],
  emit: [
    'toggleSidebar',
  ],
  methods: {
    toggleSidebar() {
      this.$emit('toggleSidebar');
    },
  },
};
</script>

<style scoped>
.sidebar-panel {
  background-color: #FBFBFF;
  box-shadow: 0 2px 4px #191919;
  display: flex;
  margin-top: 0.5em;
  height: 97.5%;
  width: 50vw;
}
</style>
