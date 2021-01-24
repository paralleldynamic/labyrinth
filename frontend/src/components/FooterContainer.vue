<template>
  <div id="footer-container">
    <footer>
      <div id="copyright-info-container">
        <p id="copyright-notice">© Patrick Spears 2021</p>
      </div>
      <!-- search functionality is not yet enabled>
      <div id="search-bar">
        <input id="search-input" type="search" name="search-key" placeholder="enter search term">
        <button id="search-submit">search</button>
      </div>
      <-->
    </footer>
  </div>
</template>

<script>
export default {
  name: 'Footer',
};
</script>

<style scoped>
footer {
  display: grid;
  grid-template-columns: 1fr 1fr;

}

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
  margin-top: 0.75em;
  margin-right: 0.75em;
  font-size: smaller;
  text-align: right;
}

#copyright-notice {
  margin: 1em;
  vertical-align: middle;
  font-size: smaller;
}
</style>
