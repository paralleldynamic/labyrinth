<template>
  <div id="footer-container">
    <footer>
      <div id="search-bar">
        <input id="search-input" type="search" name="search-key" placeholder="enter search term">
        <button id="search-submit">search</button>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style scoped>
#footer-container {
  background-color: #E5E7E9;
  height: var(--footer-container-height);
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  box-shadow: 0 -1px 2px rgba(0,0,0,0.19);
}

#search-bar {
  vertical-align: middle;
  float: right;
  padding-right: 1em;
  padding-top: 0.5em;
  padding-bottom: 0.5em;
}
</style>
