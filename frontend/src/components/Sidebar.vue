<template>
  <transition name="slide">
    <div class="sidebar-mask" @click="toggleSidebar" v-if="show">
      <div @click.stop
           class="sidebar-panel">
        <slot />
      </div>
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
.sidebar-mask {
  width: 100%;
  height: 100%;
  display: grid;
}

.sidebar-panel {
  width: 100%;
  height: 100%;
  min-width: 100%;
  background-color: #FBFBFF;
  box-shadow: 0 2px 4px #191919;
}
</style>
