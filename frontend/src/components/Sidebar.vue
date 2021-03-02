<template>
  <div class="sidebar-wrapper" v-if="show">
    <div class="sidebar">
      <div class="sidebar-header">
        <slot name="sidebar-header" />
      </div>
      <div class="sidebar-content">
        <slot name="sidebar-content" />
      </div>
      <div class="sidebar-footer">
        <slot name="sidebar-footer" />
      </div>
    </div>
  </div>
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
.sidebar-wrapper {
  background-color: #FBFBFF;
  box-shadow: 0 2px 4px #191919;
  display: flex;
  margin-top: 0.5em;
  height: 97.5%;
  width: 50vw;
}

.sidebar {
  width: 100%;
  margin: 1em;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(10, 1fr);
  text-align: center;
}

.sidebar-header {
  grid-area: 1 / 1 / 2 / 6;
}

.sidebar-content {
  grid-area: 2 / 1 / 10 / 6;
}

.sidebar-footer {
  grid-area: 10 / 1 / 11 / 6;
}

.sidebar-content > button {
  width: 80%;
  justify-self: center;
  text-align: center;
}
</style>
