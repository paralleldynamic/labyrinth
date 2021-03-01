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
.slide-enter-active,
.slide-leave-active
{
    transition: transform 0.2s ease;
}

.slide-enter,
.slide-leave-to {
    transform: translateX(-100%);
    transition: all 150ms ease-in 0s
}
</style>
