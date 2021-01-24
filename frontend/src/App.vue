<template>
  <Header />
  <div id="page-content">
    <router-view/>
  </div>
</template>

<script>
import Header from '@/components/Header.vue';

export default {
  components: {
    Header,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#header {
  left: 0;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 9999999;
  border-block-color: black;
}

#header-nav-bar {
  border-bottom: 1 px solid #ccc;
  height: 60px;
  clear: both;
  width: 100%;
}

#header a {
  font-weight: bold;
  color: #2c3e50;
}

#header a.router-link-exact-active {
  color: #42b983;
}
</style>
