<template>
  <transition name="slide">
    <div class="sidebar-mask" @click="toggleSidebar" v-if="show">
      <div v-if="show"
          @click.stop
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
  width: 50vw;
  height: 100vh;
  display: grid;
}

.sidebar-panel {
  width: 100%;
  height: 100%;
  /* border: 3px solid #191919; */
  background-color: #FBFBFF;
  box-shadow: 0 2px 4px #191919;
}
</style>
