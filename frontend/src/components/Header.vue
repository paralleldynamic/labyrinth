<template>
  <div id="header-container">
    <header>
      <nav id="navbar-menu">
        <div>
          <h1 id="navbar-title">the labyrinth</h1>
        </div>
        <div id="navbar-menu-items-container">
          <router-link class="navbar-menu-item" to="/">Homes</router-link>
          <router-link class="navbar-menu-item" to="/about">About</router-link>
          <router-link class="navbar-menu-item" to="/games">Games</router-link>
          <router-link class="navbar-menu-item" to="/campaigns">Campaigns</router-link>
          <router-link class="navbar-menu-item" to="/stories">Stories</router-link>
        </div>
      </nav>
    </header>
  </div>
</template>

<script>
export default {
  name: 'Header',
  components: {
  },
};
</script>

<style scoped>
#header-container {
  background-color: #E5E7E9;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: var(--header-container-height);
  box-shadow: 0 1px 2px rgba(0,0,0,0.19);
}

#navbar-title {
  margin: 0.25em;
  margin-bottom: 0.4em;
}
#navbar-menu {
  display: block;
  font-size: small;
  text-transform: lowercase;
  text-align: center;
}

#navbar-menu-items-container {

}

.navbar-menu-item {
  display: inline;
  margin: 0.5em;
  text-decoration: none;
  color: inherit;
}

.navbar-menu-item:hover {
  font-size: smaller;
  font-weight: bolder;
}
</style>
