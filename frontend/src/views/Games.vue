<template>
  <div class="canvas">
    <Canvas />
  </div>
</template>

<script>
// @ is an alias to /src
import Canvas from '../components/Canvas.vue';

export default {
  name: 'Games',
  components: {
    Canvas,
  },
};
</script>
