<template>
  <div id="footer-container">
    <footer>
      <div id="copyright-info-container">
        <p id="copyright-notice">© Patrick Spears 2021</p>
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
  background-color: #FBFBFF;
  height: var(--footer-container-height);
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  box-shadow: 0 -1px 2px #191919;
}

#copyright-notice {
  margin: 1em;
  vertical-align: middle;
  font-size: smaller;
}
</style>
